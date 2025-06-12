* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddOperator.html

#  [QueryEngine<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).AddOperator
Leave feedback
Suggest a change
## Success!
Thank you for helping us improve the quality of Unity Documentation. Although we cannot accept all submissions, we do read each suggested change from our users and will make updates where applicable.
Close
## Submission failed
For some reason your suggested change could not be submitted. Please <a>try again</a> in a few minutes. And thank you for taking the time to help us improve the quality of Unity Documentation.
Close
Your name Your email Suggestion* Submit suggestion
Cancel
## Declaration
public void AddOperator(string op); 
### Parameters
Parameter | Description  
---|---  
op | The operator identifier.  
### Description
Adds a custom filter operator.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_QueryEngine_AddOperator
{
    static List<MyObjectType> s_Data;

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)/AddOperator")]
    public static void RunExample()
    {
        // Set up the query engine
        var queryEngine = new QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType>();
        queryEngine.AddFilter("id", myObj => myObj.id);
        queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });

        // Add a new operator token
        const string op = "%";
        queryEngine.AddOperator(op);

        // Define what this operator does, and which types it operates on.
        queryEngine.AddOperatorHandler(op, (int ev, int fv) => ev % fv == 0);

        s_Data = new List<MyObjectType>()
        {
            new MyObjectType { id = 0, name = "Test 1", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 0), active = false },
            new MyObjectType { id = 1, name = "Test 2", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 1), active = true },
            new MyObjectType { id = 2, name = "Test 3", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1, 0), active = false },
            new MyObjectType { id = 3, name = "Test 4", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1.2f, 0), active = false },
        };

        // Find all items that have an id divisible by 2
        var query = queryEngine.ParseQuery("id%2");
        var filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 2, $"There should be 2 items in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[0]), "Test 1 should be in the list as its id is divisible by 2.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[2]), "Test 3 should be in the list as its id is divisible by 2.");

        {
            // Get an operator based on its token and add some handlers on it.
            var operatorToken = "%";
            var operatorObject = queryEngine.GetOperator(operatorToken);
            if (operatorObject.valid)
                operatorObject.AddHandler((float ev, float fv) => Math.Abs(ev % fv) < 0.0000001f);
        }

        {
            // Remove an operator based on its token
            var operatorToken = "%";
            queryEngine.RemoveOperator(operatorToken);
        }

        query = queryEngine.ParseQuery("id%2");
        filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 0, $"There should be 0 items in the filtered list but found {filteredData.Count} items.");
    }

    class MyObjectType
    {
        public int id { get; set; }
        public string name { get; set; } = string.Empty;
        public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position { get; set; } = Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html);
        public bool active { get; set; }

        public override string ToString()
        {
            return $"({id}, {name}, ({position.x}, {position.y}), {active})";
        }
    }
}

```

* * *
