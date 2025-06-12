* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.SetDefaultParamFilter.html

#  [QueryEngine<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).SetDefaultParamFilter
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
public void SetDefaultParamFilter(Func<TData,string,string,string,string,bool> handler); 
### Parameters
Parameter | Description  
---|---  
handler | Callback used to handle the function filter. Takes an object of type TData, the filter identifier, the parameter, the operator, and the filter value, and returns a boolean indicating if the filter passed or not.  
### Description
Sets the default filter handler for function filters that were not registered.
```
using System.Collections.Generic;
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_QueryEngine_SetDefaultParamFilter
{
    static List<MyObjectType> s_Data;

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)/SetDefaultParamFilter")]
    public static void RunExample()
    {
        // Set up the query engine
        var queryEngine = new QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType>();
        queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });

        // Add a filter for MyObjectType.id that supports all operators
        queryEngine.AddFilter("id", myObj => myObj.id);

        // Register a default filter handler for any filter with parameters.
        queryEngine.SetDefaultParamFilter((myObj, filterId, paramValue, operatorToken, filterValue) =>
        {
            if (myObj.property.name != filterId)
                return false;

            if (myObj.property.type == PropertyType.Integer_Array)
            {
                if (!(myObj.property.value is int[] integerArray))
                    return false;
                if (!int.TryParse(paramValue, out var indexValue))
                    return false;
                if (!int.TryParse(filterValue, out var filterValueInt))
                    return false;
                if (indexValue < 0 || indexValue >= integerArray.Length)
                    return false;
                switch (operatorToken)
                {
                    case "=": return integerArray[indexValue] == filterValueInt;
                    case "!=": return integerArray[indexValue] != filterValueInt;
                    case "<": return integerArray[indexValue] < filterValueInt;
                    case ">": return integerArray[indexValue] > filterValueInt;
                    case "<=": return integerArray[indexValue] <= filterValueInt;
                    case ">=": return integerArray[indexValue] >= filterValueInt;
                    default: return false;
                }
            }

            return false;
        });

        s_Data = new List<MyObjectType>()
        {
            new MyObjectType { id = 0, property = new Property("values", PropertyType.Integer_Array, new int[] {0, 2, 42}) },
            new MyObjectType { id = 1, property = new Property("weights", PropertyType.Integer_Array, new int[] {1000, 250, 400}) }
        };

        // Find all items that have the property "values" higher than 10 at index 2
        var query = queryEngine.ParseQuery("values(2)>10");
        var filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[0]), "The first item should be in the filtered list since its property \"values\" has a value higher than 10 at index 2.");
    }

    enum PropertyType
    {
        Integer,
        String,
        Integer_Array
    }
    struct Property
    {
        public string name { get; }
        public PropertyType type { get; }
        public object value { get; set; }

        public Property(string name, PropertyType type, object value)
        {
            this.name = name;
            this.type = type;
            this.value = value;
        }
    }

    class MyObjectType
    {
        public int id { get; set; }
        public string name { get; set; } = string.Empty;
        public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position { get; set; } = Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html);
        public bool active { get; set; }
        public Property property { get; set; }

        public override string ToString()
        {
            return $"({id}, {name}, ({position.x}, {position.y}), {active})";
        }
    }
}

```

* * *
