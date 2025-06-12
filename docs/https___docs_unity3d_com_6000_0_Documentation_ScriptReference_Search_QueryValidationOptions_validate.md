* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryValidationOptions-validateFilters.html

#  [QueryValidationOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryValidationOptions.html).validateFilters
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
validateFilters; 
### Description
Boolean indicating if filters should be validated. Default is false.
If true and [skipUnknownFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryValidationOptions-skipUnknownFilters.html) is false, unknown filters will generate errors if no default handler is provided with [QueryEngine.SetDefaultFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.SetDefaultFilter.html).
```
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_QueryValidationOptions_validateFilters
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/QueryValidationOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryValidationOptions.html)/validateFilters")]
    public static void RunExample()
    {
        // Set up the query validation options with no filter validation
        var validationOptions = new QueryValidationOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryValidationOptions.html) { validateFilters = false };

        // Set up the query engine
        var queryEngine = new QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType>(validationOptions);
        queryEngine.AddFilter("id", myObj => myObj.id);
        queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });

        // Parse a query with the filter "id". There shouldn't be any errors
        var query = queryEngine.ParseQuery("id>10");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(query.valid, $"Query \"{query.text}\" should be valid.");

        // Because the QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html) doesn't validate filters, no other filters will generate an error when parsed.
        query = queryEngine.ParseQuery("name:MyName");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(query.valid, $"Query \"{query.text}\" should be valid.");
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
