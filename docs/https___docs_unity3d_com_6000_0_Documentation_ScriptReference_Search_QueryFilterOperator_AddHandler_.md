* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryFilterOperator.AddHandler.html

#  [QueryFilterOperator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryFilterOperator.html).AddHandler
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
public [Search.QueryFilterOperator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryFilterOperator.html) AddHandler(Func<TFilterVariable,TFilterConstant,bool> handler); 
## Declaration
public [Search.QueryFilterOperator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryFilterOperator.html) AddHandler(Func<TFilterVariable,TFilterConstant,stringComparison,bool> handler); 
### Parameters
Parameter | Description  
---|---  
handler | Callback to handle the operation. Takes a TFilterVariable (the value returned by the filter handler, it will vary for each element), a TFilterConstant (right-hand side value of the operator, which is constant), and a StringComparison option and returns a boolean indicating if the filter passes or not.  
### Returns
**QueryFilterOperator** The current [QueryFilterOperator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryFilterOperator.html). 
### Description
Adds a custom filter operator handler.
<TFilterVariable>: The type of the operator's left-hand side operand. This is the type returned by a filter handler.  
  
<TFilterConstant>: The type of the operator's right-hand side operand.  
  
An operator handler is a function that is executed for a particular operator (for example "=") with specific type requirements. The operator handler is chosen by the return value of the filter handler (see [AddFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddFilter.html)) that is identified when parsing the query, and the type of the filter value.
```
// Add a new modulo operator on this filter
var op = "%";
queryEngine.TryGetFilter("id", out var filter);
filter.AddOperator(op)
    .AddHandler((int ev, int fv) => ev % fv == 0)
    .AddHandler((float ev, float fv) => Math.Abs(ev % fv) < 0.00000001f);

```

Here is an example where we override the behavior of the "=" operator for all filters when strings are involved, by doing a regular expression search instead of the traditional match.
```
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_QueryEngine_RegexValue
{
    static QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType> SetupQueryEngine()
    {
        var queryEngine = new QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType>();
        queryEngine.AddFilter("id", myObj => myObj.id);
        queryEngine.AddFilter("n", myObj => myObj.name);
        queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });

        // Override the = operators to do a regex match
        var op = queryEngine.GetOperator("=");
        op.AddHandler((string ev, string fv) => RegexMatch(fv, ev));

        return queryEngine;
    }

    static bool RegexMatch(string pattern, string source)
    {
        var match = Regex.Match(source, pattern);
        return match.Success;
    }

    static string[] s_Words = new[] { "bob", "cat", "car", "happy", "sad", "squirrel", "pizza", "dog", "over", "bing", "bong" };
    static IEnumerable<MyObjectType> GenerateData(int count)
    {
        for (var i = 0; i < count; ++i)
        {
            var wordCount = Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(1, 6);
            var words = new List<string>();
            for (var j = 0; j < wordCount; ++j)
                words.Add(s_Words[Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0, s_Words.Length)]);

            var name = string.Join(" ", words);
            var id = $"{Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0, 1000)}-{s_Words[Random.Range[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Random.Range.html)(0, s_Words.Length)]}";
            yield return new MyObjectType() { id = id, name = name };
        }
    }

    static void FilterData(string text, QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType> queryEngine, IEnumerable<MyObjectType> data)
    {
        var query = queryEngine.ParseQuery(text);
        if (!query.valid)
        {
            foreach (var queryError in query.errors)
                Debug.LogFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogFormat.html)(LogType.Error[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.Error.html), LogOption.NoStacktrace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogOption.NoStacktrace.html), null, $"Error[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/PackageManager.Error.html) parsing query at position {queryError.index}: {queryError.reason}");

            return;
        }

        var filteredData = query.Apply(data).ToList();
        var escapedText = text.Replace("{", "{{").Replace("}", "}}");
        Debug.LogFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogFormat.html)(LogType.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.Log.html), LogOption.NoStacktrace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogOption.NoStacktrace.html), null, $"Query \"{escapedText}\" yielded {filteredData.Count} result{(filteredData.Count > 1 ? "s" : "")}");
        foreach (var filteredObject in filteredData)
            Debug.LogFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogFormat.html)(LogType.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.Log.html), LogOption.NoStacktrace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogOption.NoStacktrace.html), null, filteredObject.ToString());
    }

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)/RegexValue")]
    public static void RunExample()
    {
        // Set up the query engine
        var queryEngine = SetupQueryEngine();

        var data = GenerateData(100);

        // Find all items with an id that match "^\\d{2}-c.+" (for example, "42-cat" or "99-car")
        // The quotes are required when using special characters like {}.
        FilterData("id=\"^\\d{2}-c.+\"", queryEngine, data);

        // Find all items with a name containing a duplicate (for example, "squirrel cat cat dog" or "pizza pizza dog")
        // The quotes are required when using special characters like {}.
        FilterData("n=(\\S+)\\s+(\\1)", queryEngine, data);
    }

    class MyObjectType
    {
        public string id { get; set; }
        public string name { get; set; } = string.Empty;

        public override string ToString()
        {
            return $"({id}, {name})";
        }
    }
}

```

* * *
