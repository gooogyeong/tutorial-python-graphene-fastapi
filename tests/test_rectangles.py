from db import RectangleModel

def test_rectangles_query(client, session):
    client, context = client

    operation="""
    {
        rectangles {
            id
            x
            y
            width
            height
        }
    }
    """

    result_before = client.execute(operation, context_value=context)

    assert len(result_before['data']['rectangles']) == 0

    rectangle1 = RectangleModel(id=1, x=10, y=10, width=10, height=10, color="red")
    rectangle2 = RectangleModel(id=2, x=10, y=10, width=10, height=10, color="red")
    
    session.add_all([rectangle1, rectangle2])
    session.commit()

    result_after = client.execute(operation, context_value=context)

    assert len(result_after['data']['rectangles']) == 2

def test_add_rectangle(client, session):
    client, context = client

    existing_rectangles = session.query(RectangleModel).all()

    operation="""
        mutation {
            addRectangle(x: 11.0, y: 12.0, width: 13.0, height: 14.0, color: "red") {
                id
                width
                height
                x
                y
                color
            }
        }
    # """

    result = client.execute(operation, context_value=context)

    remaining_rectangles = session.query(RectangleModel).all()

    assert result['data']['addRectangle'] == {'id': '1', 'width': 13.0, 'height': 14.0, 'x': 11.0, 'y': 12.0, 'color': 'red'}

    assert len(remaining_rectangles) == len(existing_rectangles) + 1

def test_delete_rectangles(client, session):
    client, context = client

    existing_rectangles = session.query(RectangleModel).all()

    rectangle1 = RectangleModel(id=100, x=10, y=10, width=10, height=10, color="red")
    rectangle2 = RectangleModel(id=101, x=10, y=10, width=10, height=10, color="red")
    
    session.add_all([rectangle1, rectangle2])
    session.commit()

    operation="""
        mutation {
            deleteRectangles(ids: ["100", "101"])
        }
    """

    result = client.execute(operation, context_value=context)

    remaining_rectangles = session.query(RectangleModel).all()

    assert result['data']['deleteRectangles'] == ['100', '101']

    assert len(remaining_rectangles) == len(existing_rectangles)
