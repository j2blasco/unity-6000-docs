* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FuzzySearch.FuzzyMatch.html

#  [FuzzySearch](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FuzzySearch.html).FuzzyMatch
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
public static bool FuzzyMatch(string pattern, string origin, ref long outScore, List<int> matches); 
## Declaration
public static bool FuzzyMatch(string pattern, string origin, List<int> matches); 
### Parameters
Parameter | Description  
---|---  
pattern | The pattern that the method is searching for in the string.  
origin | The string the method is searching.  
outScore | If there is a match, this parameter contains the match score. The higher the match score, the closer the pattern matched a part of the given string.  
matches | List of indices in the string where the pattern was found.  
### Returns
**bool** Returns true if a match was found. 
### Description
Performs a fuzzy search for a pattern on a string.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_FuzzySearch_FuzzyMatch
{
    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/FuzzySearch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FuzzySearch.html)/FuzzyMatch")]
    public static void Run()
    {
        const string pattern = "exfsfm";
        const string toBeSearched = nameof(Example_FuzzySearch_FuzzyMatch);

        long score = 0;
        if (FuzzySearch.FuzzyMatch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FuzzySearch.FuzzyMatch.html)(pattern, toBeSearched, ref score))
            Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(score == 309);

        // This allocated list can be reused for multiple calls to FuzzyMatch
        var matches = new List<int>();
        if (FuzzySearch.FuzzyMatch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FuzzySearch.FuzzyMatch.html)(pattern, toBeSearched, ref score, matches))
        {
            var formattedMatch = RichTextFormatter.FormatSuggestionTitle(toBeSearched, matches);
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)($"Found fuzzy pattern <i>{pattern}</i> in {formattedMatch} with indices " +
                $"{string.Join(",", matches.Select(m => m.ToString()))} and got a score of <b>{score}</b>");
        }
    }

    static class RichTextFormatter
    {
        static readonly char[] cache_result = new char[1024];
        public static string HighlightColorTag = EditorGUIUtility.isProSkin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-isProSkin.html) ? "<color=#FF6100>" : "<color=#EE4400>";
        public static string HighlightColorTagSpecial = EditorGUIUtility.isProSkin[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/EditorGUIUtility-isProSkin.html) ? "<color=#FF6100>" : "<color=#BB1100>";

        public static string FormatSuggestionTitle(string title, List<int> matches)
        {
            return FormatSuggestionTitle(title, matches, HighlightColorTag, HighlightColorTagSpecial);
        }

        public static string FormatSuggestionTitle(string title, List<int> matches, string selectedTextColorTag, string specialTextColorTag)
        {
            const string closingTag = "</color>";
            int openCharCount = specialTextColorTag.Length;
            int closingCharCount = closingTag.Length;

            var N = title.Length + matches.Count * (closingCharCount + openCharCount);
            var MN = matches.Count;

            var result = cache_result;
            if (N > cache_result.Length)
                result = new char[N];

            int t_i = 0;
            int t_j = 0;
            int t_k = 0;
            string tag = null;
            var needToClose = false;

            for (int guard = 0; guard < N; ++guard)
            {
                if (tag == null && needToClose == false && t_k < MN)
                {
                    var indx = matches[t_k];
                    if (indx == t_i || indx == -t_i)
                    {
                        tag = (indx < 0) ? specialTextColorTag : selectedTextColorTag;
                        ++t_k;
                    }
                }

                if (tag != null)
                {
                    result[guard] = tag[t_j++];

                    if (t_j >= tag.Length)
                    {
                        if (tag != closingTag)
                            needToClose = true;

                        tag = null;
                        t_j = 0;
                    }
                }
                else
                {
                    result[guard] = title[Math.Min(t_i++, title.Length - 1)];

                    if (needToClose)
                    {
                        tag = closingTag;
                        needToClose = false;
                    }
                }
            }

            return new string(result, 0, N);
        }
    }
}


```

This can also be used easily in the context of a [QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html) to enable fuzzy search.
```
using System.Collections.Generic;
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_QueryEngine_FuzzyMatch
{
    static QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType> SetupQueryEngine()
    {
        var queryEngine = new QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType>();
        queryEngine.AddFilter("id", myObj => myObj.id);
        queryEngine.AddFilter("n", myObj => myObj.name);
        queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });

        // Add a new operator token for fuzzy matching
        const string op = "~=";
        queryEngine.AddOperator(op);

        // Define what this operator does, and which types it operates on.
        queryEngine.AddOperatorHandler(op, (string ev, string fv) => FuzzySearch.FuzzyMatch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FuzzySearch.FuzzyMatch.html)(fv, ev));

        // Set the word matcher function to also support fuzzy matching
        queryEngine.SetSearchWordMatcher((word, exactMatch, stringComparison, searchDataCallbackValue) =>
        {
            if (exactMatch)
                return string.Equals(word, searchDataCallbackValue, stringComparison);
            return FuzzySearch.FuzzyMatch[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.FuzzySearch.FuzzyMatch.html)(word, searchDataCallbackValue);
        });

        return queryEngine;
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
        Debug.LogFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogFormat.html)(LogType.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.Log.html), LogOption.NoStacktrace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogOption.NoStacktrace.html), null, $"Query \"{text}\" yielded {filteredData.Count} result{(filteredData.Count > 1 ? "s" : "")}");
        foreach (var filteredObject in filteredData)
            Debug.LogFormat[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.LogFormat.html)(LogType.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogType.Log.html), LogOption.NoStacktrace[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/LogOption.NoStacktrace.html), null, filteredObject.ToString());
    }

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)/FuzzyMatch")]
    public static void RunExample()
    {
        // Set up the query engine
        var queryEngine = SetupQueryEngine();

        var data = GenerateData(100);

        // Find all items with a name that match "ccs" (for example, "cat car squirrel" or "car cat sad")
        FilterData("n~=ccs", queryEngine, data);

        // Find all items with a name or an id that match "bob" (for example, "bob", "42-bob" or "bing over bong")
        FilterData("bob", queryEngine, data);
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
