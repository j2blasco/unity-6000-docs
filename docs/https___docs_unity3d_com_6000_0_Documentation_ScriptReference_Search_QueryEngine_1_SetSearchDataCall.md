* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.SetSearchDataCallback.html

#  [QueryEngine<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).SetSearchDataCallback
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
public void SetSearchDataCallback(Func<TData,IEnumerable<string>> getSearchDataCallback); 
## Declaration
public void SetSearchDataCallback(Func<TData,IEnumerable<string>> getSearchDataCallback, stringComparison stringComparison); 
### Parameters
Parameter | Description  
---|---  
getSearchDataCallback | Callback used to get the data to be matched against the search words. Takes an object of type TData and returns an IEnumerable of strings.  
stringComparison | String comparison options.  
### Description
Sets the callback used to fetch the data that is matched against the search words.
This function lets you register a callback that will be called on each element of the data set you are trying to filter, in order to retrieve the search data that will be compared against search words (for example, words that are not filters). Here is an example:
```
// Set up what data from objects of type MyObjectType will be matched against search words
queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });

```

For a more complete example on how to use this function, see [QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).
* * *
## Declaration
public void SetSearchDataCallback(Func<TData,IEnumerable<string>> getSearchDataCallback, Func<string,string> searchWordTransformerCallback, stringComparison stringComparison); 
### Parameters
Parameter | Description  
---|---  
getSearchDataCallback | Callback used to get the data to be matched against the search words. Takes an object of type TData and returns an IEnumerable of strings.  
searchWordTransformerCallback | Callback used to transform a search word during the query parsing. Useful when doing lowercase or uppercase comparison. Can return null or an empty string to remove the word from the query.  
stringComparison | String comparison options.  
### Description
Sets the callback used to fetch the data that is matched against the search words.
This function lets you register a callback that will be called on each element of the data set you are trying to filter, in order to retrieve the search data that will be compared against search words (for example, words that are not filters). Also, it gives you tha ability to apply a transformation on the search words themselves to prepare the comparison. This transformation is only done once when the query is parsed.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_QueryEngine_SetSearchDataCallback
{
    static List<MyObjectType> s_Data;

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)/SetSearchDataCallback")]
    public static void RunExample()
    {
        // Set up the query engine
        var queryEngine = new QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType>();

        // Set the search data callback with a word transformer.
        // The word transformer will make sure that the words used for comparison are already converted to lowercase,
        // which will increase performance by doing comparisons with Ordinal instead of OrdinalIgnoreCase
        queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name }, word => word.ToLowerInvariant(), StringComparison.Ordinal);

        s_Data = new List<MyObjectType>()
        {
            new MyObjectType { id = 0, name = "Test 1", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 0), active = false },
            new MyObjectType { id = 1, name = "Test 2", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 1), active = true },
            new MyObjectType { id = 2, name = "Test 3", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1, 0), active = false },
            new MyObjectType { id = 3, name = "Test 4", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1.2f, 0), active = false },
        };

        // Find all items that contain "test" in the search data
        var query = queryEngine.ParseQuery("Test");
        var filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 4, $"There should be 4 items in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[0]), "Test 1 should be in the list as its name contains \"test\".");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[1]), "Test 2 should be in the list as its name contains \"test\".");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[2]), "Test 3 should be in the list as its name contains \"test\".");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[3]), "Test 4 should be in the list as its name contains \"test\".");

        // Find all items that have exactly "test 4" in the search data.
        query = queryEngine.ParseQuery("!\"Test 4\"");
        filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[3]), "Test 4 should be in the list as its name is exactly \"test 4\".");
    }

    class MyObjectType
    {
        public int id { get; set; }

        string m_Name = string.Empty;
        public string name
        {
            get => m_Name;
            set => m_Name = value.ToLowerInvariant();
        }

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
