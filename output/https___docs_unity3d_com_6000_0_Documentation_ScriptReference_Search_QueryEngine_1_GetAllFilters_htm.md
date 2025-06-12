* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.GetAllFilters.html

#  [QueryEngine<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).GetAllFilters
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
public IEnumerable<IQueryEngineFilter> GetAllFilters(); 
### Returns
**IEnumerable <IQueryEngineFilter>** An enumerable of [IQueryEngineFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IQueryEngineFilter.html). 
### Description
Get all filters added on this [QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).
This method returns all the filters that were added on the [QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).
```
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_QueryEngine_GetAllFilters
{
    static QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType> SetupQueryEngine()
    {
        // Set up the query engine
        var queryEngine = new QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType>();

        // Add a filter for MyObjectType.id that supports all operators
        queryEngine.AddFilter("id", myObj => myObj.id);
        // Add a filter for MyObjectType.name that supports only contains (:), equal (=) and not equal (!=)
        queryEngine.AddFilter("n", myObj => myObj.name, new[] { ":", "=", "!=" });
        // Add a filter for MyObjectType.active that supports only equal and not equal
        queryEngine.AddFilter("a", myObj => myObj.active, new[] { "=", "!=" });
        // Add a filter for the computed property magnitude that supports equal, not equal, lesser, greater, lesser or equal and greater or equal.
        queryEngine.AddFilter("m", myObj => myObj.position.magnitude, new[] { "=", "!=", "<", ">", "<=", ">=" });

        // Set up what data from objects of type MyObjectType will be matched against search words
        queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });

        return queryEngine;
    }

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)/GetAllFilters")]
    public static void RunExample()
    {
        var queryEngine = SetupQueryEngine();

        var allFilters = queryEngine.GetAllFilters();
        foreach (var filter in allFilters)
        {
            Debug.LogFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogFormat.html)(LogType.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.Log.html), LogOption.NoStacktrace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogOption.NoStacktrace.html), null, $"Filter: {filter.token} - Supported operators: {(filter.supportedOperators?.Any() ?? false ? "[" + string.Join(", ", filter.supportedOperators) + "]" : "All")}");
        }

        // Get the filter corresponding to the token "id"
        if (!queryEngine.TryGetFilter("id", out var idFilter))
            Debug.LogError[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogError.html)("The filter \"id\" should have been found.");

        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(idFilter != null, "Filter \"id\" should not be null.");

        // Remove the filter with token "id"
        var token = "id";
        queryEngine.RemoveFilter("id");

        var found = queryEngine.TryGetFilter(token, out idFilter);
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(found == false, "Filter \"id\" should not be found.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(idFilter == null, "Filter \"id\" should be null.");
    }

    /// <summary>
    /// Custom type. This is the type of objects that will be searched by the QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html).
    /// </summary>
    class MyObjectType
    {
        public int id { get; set; }
        public string name { get; set; }
        public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position { get; set; }
        public bool active { get; set; }

        public MyObjectType()
        {
            id = 0;
            name = "";
            position = Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html);
            active = false;
        }

        public override string ToString()
        {
            return $"({id}, {name}, ({position.x}, {position.y}), {active})";
        }
    }
}

```

* * *
