from app.graph import graph

result = graph.invoke({
    "user_input": "Met Dr. Sharma yesterday at 2 PM. Discussed Product X. Shared one brochure. Doctor was positive. Follow up next week."
})

print(result)