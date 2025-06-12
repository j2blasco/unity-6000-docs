* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddTypeParser.html

#  [QueryEngine<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).AddTypeParser
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
public void AddTypeParser(Func<string,ParseResult<TFilterConstant>> parser); 
### Parameters
Parameter | Description  
---|---  
parser | Callback used to determine if a string can be converted into TFilterConstant. Takes a string and returns a ParseResult object. This contains the success flag, and the converted value if it succeeds.  
### Description
Adds a type parser that parses a string and returns a custom type. Used by custom operator handlers (see [AddOperatorHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddOperatorHandler.html)).
<TFilterConstant>: The type of the parsed operand that is on the right-hand side of the operator.
```
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_QueryEngine_AddTypeParser
{
    static List<MyObjectType> s_Data;

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)/AddTypeParser")]
    public static void RunExample()
    {
        // Set up the query engine
        var queryEngine = new QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType>();
        queryEngine.AddFilter("id", myObj => myObj.id);
        queryEngine.AddFilter("p", myObj => myObj.position, new[] { "=", "!=" });
        queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });

        // Add a new type parser for Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) written as "[x, y]"
        queryEngine.AddTypeParser<Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)>(s =>
        {
            // If the format requirement is not met, return a failure.
            if (!s.StartsWith("[") || !s.EndsWith("]"))
                return ParseResult<Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)>.none;

            var trimmed = s.Trim('[', ']');
            var vectorTokens = trimmed.Split(',');
            var vectorValues = vectorTokens.Select(token => float.Parse(token, CultureInfo.InvariantCulture.NumberFormat)).ToList();
            if (vectorValues.Count != 2)
                return ParseResult<Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)>.none;
            var vector = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(vectorValues[0], vectorValues[1]);

            // When the conversion succeeds, return a success.
            return new ParseResult<Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)>(true, vector);
        });
        queryEngine.AddOperatorHandler("=", (Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) ev, Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) fv) => ev == fv);
        queryEngine.AddOperatorHandler("!=", (Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) ev, Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) fv) => ev != fv);

        s_Data = new List<MyObjectType>()
        {
            new MyObjectType { id = 0, name = "Test 1", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 0), active = false },
            new MyObjectType { id = 1, name = "Test 2", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 1), active = true },
            new MyObjectType { id = 2, name = "Test 3", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1, 0), active = false },
            new MyObjectType { id = 3, name = "Test 4", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1.2f, 0), active = false },
        };

        // Find all items that are located at position [0, 1]
        var query = queryEngine.ParseQuery("p=\"[0, 1]\"");
        var filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[1]), "Test 2 should be in the list as its position [0, 1].");
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
