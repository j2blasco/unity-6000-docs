* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html

# QueryEngine<T0>
class in UnityEditor.Search
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
### Description
A QueryEngine defines how to build a query from an input string. It can be customized to support custom filters and operators.
<TData>: The filtered data type.
```
using System.Collections.Generic;
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_QueryEngine
{
    static List<MyObjectType> s_Data;

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

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)/Class")]
    public static void RunExample()
    {
        s_Data = GenerateExampleData();
        var queryEngine = SetupQueryEngine();
        TestFiltering(queryEngine, s_Data);
    }

    static void TestFiltering(QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType> queryEngine, IEnumerable<MyObjectType> inputData)
    {
        // Find objects that have an id > 2 and are active
        var filteredData = FilterData("id>2 a=true", queryEngine, inputData);
        ValidateData(filteredData, s_Data.Where(myObj => myObj.id > 2 && myObj.active));

        // Find objects that are not active and have a name that contains Test
        filteredData = FilterData("a=false n:Test", queryEngine, inputData);
        ValidateData(filteredData, s_Data.Where(myObj => myObj.name.Contains("Test") && !myObj.active));

        // Find objects that have a magnitude higher than 1 or the id 0.
        filteredData = FilterData("m>1 or id=0", queryEngine, inputData);
        ValidateData(filteredData, s_Data.Where(myObj => myObj.position.magnitude > 1f || myObj.id == 0));
    }

    static IEnumerable<MyObjectType> FilterData(string inputQuery, QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType> queryEngine, IEnumerable<MyObjectType> inputData)
    {
        // Parse the query string into a query operation
        var query = queryEngine.ParseQuery(inputQuery);

        // If the query is not valid, print all errors and return an empty data set
        if (!query.valid)
        {
            foreach (var queryError in query.errors)
            {
                Debug.LogFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogFormat.html)(LogType.Error[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.Error.html), LogOption.NoStacktrace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogOption.NoStacktrace.html), null, $"Error[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Error.html) parsing input at {queryError.index}: {queryError.reason}");
            }

            return new List<MyObjectType>();
        }

        // Apply the query on a data set and get the filtered result.
        var filteredData = query.Apply(inputData);
        return filteredData;
    }

    static void ValidateData(IEnumerable<MyObjectType> filteredData, IEnumerable<MyObjectType> expectedData)
    {
        var filteredDataArray = filteredData.ToArray();
        var expectedDataArray = expectedData.ToArray();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredDataArray.Length == expectedDataArray.Length, $"Filtered data should have {expectedDataArray.Length} elements.");
        if (filteredDataArray.Length != expectedDataArray.Length)
            return;

        for (var i = 0; i < expectedDataArray.Length; i++)
        {
            Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredDataArray[i] == expectedDataArray[i], $"{filteredDataArray[i]} should be equal to {expectedDataArray[i]}");
        }
    }

    static List<MyObjectType> GenerateExampleData()
    {
        var data = new List<MyObjectType>()
        {
            new MyObjectType { id = 0, name = "Test 1", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 0), active = false },
            new MyObjectType { id = 1, name = "Test 2", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 1), active = true },
            new MyObjectType { id = 2, name = "Test 3", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1, 0), active = false },
            new MyObjectType { id = 3, name = "Test 4", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1, 1), active = true },
            new MyObjectType { id = 4, name = "Test 5", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(2, 0), active = false },
            new MyObjectType { id = 5, name = "Test 6", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 2), active = true }
        };

        return data;
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
### Properties
Property | Description  
---|---  
[globalStringComparison](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1-globalStringComparison.html) | Global string comparison options for word matching and filter handling (if not overridden).  
[searchDataCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1-searchDataCallback.html) | The callback used to get the data to match to the search words.  
[searchDataOverridesStringComparison](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1-searchDataOverridesStringComparison.html) | Indicates if word/phrase matching uses searchDataStringComparison or not.  
[searchDataStringComparison](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1-searchDataStringComparison.html) | String comparison options for word/phrase matching.  
[searchWordMatcher](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1-searchWordMatcher.html) | The function used to match the search data against the search words.  
[skipIncompleteFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1-skipIncompleteFilters.html) | Boolean. Indicates if incomplete filters should be skipped. If true, filters are skipped. If false and validateFilters is true, incomplete filters will generate errors when parsed.  
[skipUnknownFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1-skipUnknownFilters.html) | Boolean. Indicates if unknown filters should be skipped. If true, unknown filters are skipped. If false and validateFilters is true, unknown filters will generate errors if no default filter handler is provided.  
[validateFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1-validateFilters.html) | Get or set if the engine must validate filters when parsing the query. Defaults to true.  
### Constructors
Constructor | Description  
---|---  
[QueryEngine_1](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1-ctor.html) | Constructs a new QueryEngine.  
### Public Methods
Method | Description  
---|---  
[AddFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddFilter.html) | Adds a new custom filter.  
[AddFiltersFromAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddFiltersFromAttribute.html) | Adds all custom filters that are identified with the method attribute TFilterAttribute.  
[AddNestedQueryAggregator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddNestedQueryAggregator.html) | Adds a new nested query aggregator. An aggregator is an operation that can be applied on a nested query to aggregate the results of the nested query according to certain criteria.  
[AddOperator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddOperator.html) | Adds a custom filter operator.  
[AddOperatorHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddOperatorHandler.html) | Adds a custom filter operator handler.  
[AddTypeParser](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddTypeParser.html) | Adds a type parser that parses a string and returns a custom type. Used by custom operator handlers (see AddOperatorHandler).  
[ClearFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.ClearFilters.html) | Removes all filters that were added on the QueryEngine.  
[GetAllFilters](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.GetAllFilters.html) | Get all filters added on this QueryEngine.  
[GetOperator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.GetOperator.html) | Get a custom operator added on the QueryEngine.  
[ParseQuery](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.ParseQuery.html) | Parses a query string into a ParsedQuery operation. This ParsedQuery operation can then be used to filter any data set of type TData.  
[RemoveFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.RemoveFilter.html) | Removes a custom filter.  
[RemoveOperator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.RemoveOperator.html) | Removes a custom operator that was added on the QueryEngine.  
[SetDefaultFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.SetDefaultFilter.html) | Sets the default filter handler for filters that were not registered.  
[SetDefaultParamFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.SetDefaultParamFilter.html) | Sets the default filter handler for function filters that were not registered.  
[SetFilterNestedQueryTransformer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.SetFilterNestedQueryTransformer.html) | Sets a filter's nested query transformer function. This function takes the result of a nested query and extracts the necessary data to compare with the filter.  
[SetGlobalStringComparisonOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.SetGlobalStringComparisonOptions.html) | Sets global string comparison options. Used for word matching and filter handling (unless overridden by filter).  
[SetNestedQueryHandler](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.SetNestedQueryHandler.html) | Sets the function that will handle nested queries. Only one handler can be set.  
[SetSearchDataCallback](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.SetSearchDataCallback.html) | Sets the callback used to fetch the data that is matched against the search words.  
[SetSearchWordMatcher](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.SetSearchWordMatcher.html) | Set the search word matching function to be used instead of the default one. Set to null to use the default.  
[TryGetFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.TryGetFilter.html) | Get a filter by its token.  
* * *
