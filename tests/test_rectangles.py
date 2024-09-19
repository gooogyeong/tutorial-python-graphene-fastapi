from db import RectangleModel

# def test_rectangles_query(client, session):
#     client, context = client

#     existing_rectangles_count = session.query(RectangleModel).all()

#     rectangle1 = RectangleModel(id=1, x=10, y=10, width=10, height=10, color="red")
#     rectangle2 = RectangleModel(id=2, x=20, y=20, width=20, height=20, color="blue")

#     session.add_all([rectangle1, rectangle2])
#     session.commit()

#     operation="""
#     {
#         rectangles {
#                 id
#                 x
#                 y
#                 width
#                 height
#         }
#     }
#     """

#     result = client.execute(operation, context_value=context)

#     # remaining_rectangles = session.query(RectangleModel).all()
#     expected_result = {}
#     assert len(result['data']['rectangles']) == 2

def test_delete_rectangles(client, session):
    client, context = client

    existing_rectangles_count = session.query(RectangleModel).all()

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

    assert len(remaining_rectangles) == len(existing_rectangles_count)
