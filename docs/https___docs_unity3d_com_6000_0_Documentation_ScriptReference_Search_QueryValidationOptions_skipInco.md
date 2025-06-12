* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryValidationOptions-skipIncompleteFilters.html

#  [QueryValidationOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryValidationOptions.html).skipIncompleteFilters
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
skipIncompleteFilters; 
### Description
Boolean indicating if incomplete filters should be skipped.
If true, incomplete filters are skipped. If false and [validateFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryValidationOptions-validateFilters.html) is true, incomplete filters will generate errors when parsed.
```
using System.Globalization;
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_QueryValidationOptions_skipIncompleteFilters
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/QueryValidationOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryValidationOptions.html)/skipIncompleteFilters")]
    public static void RunExample()
    {
        // Set up the query validation options with filter validation and incomplete filter skipping.
        var validationOptions = new QueryValidationOptions[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryValidationOptions.html) { validateFilters = true, skipIncompleteFilters = true};

        // Set up the query engine
        var queryEngine = new QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType>(validationOptions);
        queryEngine.AddFilter("id", myObj => myObj.id);
        queryEngine.AddFilter("dist", (myObj, paramPosition) =>
        {
            // Compute the distance from the position that was retrieved in the parameter transformer
            var vec = myObj.position - paramPosition;
            return vec.magnitude;
        }, paramStringValue =>
            {
                // Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) the parameter from a string to a usable Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)
                if (paramStringValue.StartsWith("[") && paramStringValue.EndsWith("]"))
                {
                    paramStringValue = paramStringValue.Trim('[', ']');
                    var vectorTokens = paramStringValue.Split(',');
                    var vectorValues = vectorTokens.Select(token => float.Parse(token, CultureInfo.InvariantCulture.NumberFormat)).ToList();
                    return new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(vectorValues[0], vectorValues[1]);
                }
                return Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html);
            }, new[] { "=", "!=", "<", ">", "<=", ">=" });
        queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });

        var dataset = new[]
        {
            new MyObjectType() { id = 0, name = "Test 1" },
            new MyObjectType() { id = 10, name = "Test 2" }
        };

        // Parse a query with the filter "id". There shouldn't be any errors
        var query = queryEngine.ParseQuery("id>10");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(query.valid, $"Query \"{query.text}\" should be valid.");

        // Because the QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html) is skipping incomplete filters, we shouldn't get any errors for filters that are not completely written yet,
        // but we should still get results for filters that are known. If we would only set validateFilters
        // to false, this query would not yield any results since the generated filter node for the incomplete filter
        // would be an automatic return false for any elements of the filtered data set.
        query = queryEngine.ParseQuery("id<10 dist(");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(query.valid, $"Query \"{query.text}\" should be valid.");
        var filteredData = query.Apply(dataset).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(dataset[0]), "Test 1 should be in the filtered list since its id is < 10");
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
