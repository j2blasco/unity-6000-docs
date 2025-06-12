* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddFilter.html

#  [QueryEngine<T0>](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).AddFilter
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
public void AddFilter(string token, Func<TData,TFilter> getDataFunc, string[] supportedOperatorType); 
## Declaration
public void AddFilter(string token, Func<TData,TFilter> getDataFunc, stringComparison stringComparison, string[] supportedOperatorType); 
### Parameters
Parameter | Description  
---|---  
token | The identifier of the filter. Typically what precedes the operator in a filter (for example, "id" in "id>=2").  
getDataFunc | Callback used to get the object that is used in the filter. Takes an object of type TData and returns an object of type TFilter.  
stringComparison | String comparison option.  
supportedOperatorType | List of supported operator tokens. This list contains the supported operator tokens. Use null or an empty list to indicate that all operators are supported.  
### Description
Adds a new custom filter.
<TData>: The type of the data that is filtered by the [QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).  
  
<TFilter>: The type of the data that is compared by the filter.  
  
Use this overload to register basic filters if you don't need to handle the operators yourself.
```
// Add a filter for MyObjectType.id that supports all operators
queryEngine.AddFilter("id", myObj => myObj.id);
// Add a filter for MyObjectType.name that supports only contains (:), equal (=) and not equal (!=)
queryEngine.AddFilter("n", myObj => myObj.name, new[] { ":", "=", "!=" });
// Add a filter for MyObjectType.active that supports only equal and not equal
queryEngine.AddFilter("a", myObj => myObj.active, new[] { "=", "!=" });
// Add a filter for the computed property magnitude that supports equal, not equal, lesser, greater, lesser or equal and greater or equal.
queryEngine.AddFilter("m", myObj => myObj.position.magnitude, new[] { "=", "!=", "<", ">", "<=", ">=" });


```

For a complete example see [QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).
* * *
## Declaration
public void AddFilter(string token, Func<TData,TParam,TFilter> getDataFunc, string[] supportedOperatorType); 
## Declaration
public void AddFilter(string token, Func<TData,TParam,TFilter> getDataFunc, stringComparison stringComparison, string[] supportedOperatorType); 
## Declaration
public void AddFilter(string token, Func<TData,TParam,TFilter> getDataFunc, Func<string,TParam> parameterTransformer, string[] supportedOperatorType); 
## Declaration
public void AddFilter(string token, Func<TData,TParam,TFilter> getDataFunc, Func<string,TParam> parameterTransformer, stringComparison stringComparison, string[] supportedOperatorType); 
### Parameters
Parameter | Description  
---|---  
token | The identifier of the filter. Typically what precedes the operator in a filter (for example, "id" in "id>=2").  
getDataFunc | Callback used to get the object that is used in the filter. Takes an object of type TData and TParam, and returns an object of type TFilter.  
parameterTransformer | Callback used to convert a string to type TParam. Used when parsing the query to convert what is passed to the function into the correct format.  
stringComparison | String comparison option.  
supportedOperatorType | List of supported operator tokens. This list contains the supported operator tokens. Use null or an empty list to indicate that all operators are supported.  
### Description
Adds a new custom filter with parameters.
<TData>: The type of the data that is filtered by the [QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).  
  
<TFilter>: The type of the data that is compared by the filter.  
  
<TParam>: The type of the data that is passed to the filter.  
  
Use this overload to register filters that accept parameters if you don't need to handle the operators yourself.
```
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_QueryEngine_AddFilter_Param
{
    static List<MyObjectType> s_Data;

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)/AddFilter_Param")]
    public static void RunExample()
    {
        // Set up the query engine
        var queryEngine = new QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType>();
        queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });

        // Add a "dist" filter to filter items based on a specified distance from a position or from another item
        queryEngine.AddFilter("dist", (myObj, paramPosition) =>
        {
            // Compute the distance from the position that was retrieved in the parameter transformer
            var vec = myObj.position - paramPosition;
            return vec.magnitude;
        }, paramStringValue =>
            {
                // Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) the parameter from a string to a usable Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)

                // If the user specified a vector
                if (paramStringValue.StartsWith("[") && paramStringValue.EndsWith("]"))
                {
                    paramStringValue = paramStringValue.Trim('[', ']');
                    var vectorTokens = paramStringValue.Split(',');
                    var vectorValues = vectorTokens.Select(token => float.Parse(token, CultureInfo.InvariantCulture.NumberFormat)).ToList();
                    return new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(vectorValues[0], vectorValues[1]);
                }

                // Treat the value as the name of an object
                var myObj = s_Data.Find(obj => obj.name == paramStringValue);
                return myObj.position;
            }, new[] { "=", "!=", "<", ">", "<=", ">=" });

        s_Data = new List<MyObjectType>()
        {
            new MyObjectType { id = 0, name = "Test 1", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 0), active = false },
            new MyObjectType { id = 1, name = "Test 2", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 1), active = true },
            new MyObjectType { id = 2, name = "Test 3", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1, 0), active = false },
            new MyObjectType { id = 3, name = "Test 4", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1.2f, 0), active = false },
        };

        // Find all items that are at a distance of 1 or greater to [0, 0]
        var query = queryEngine.ParseQuery("dist([0, 0])>=1");
        var filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 3, $"There should be 3 items in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(!filteredData.Contains(s_Data[0]), "Test 1 should not be in the list as its distance to [0, 0] is < 1.");

        // Find all items that are at a distance smaller than 1 to "Test 3", but not "Test 3" itself
        query = queryEngine.ParseQuery("dist(Test 3)<1 -\"Test 3\"");
        filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[3]), "Test 4 should be in the list as its distance to Test 3 is < 1.");
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
## Declaration
public void AddFilter(string token, Func<TData,string,TFilter,bool> filterResolver, string[] supportedOperatorType); 
### Parameters
Parameter | Description  
---|---  
token | The identifier of the filter. Typically what precedes the operator in a filter (for example, "id" in "id>=2").  
filterResolver | Callback used to handle any operators for this filter. Takes an object of type TData, the operator token and the filter value, and returns a boolean indicating if the filter passed or not.  
supportedOperatorType | List of supported operator tokens. This list contains the supported operator tokens. Use null or an empty list to indicate that all operators are supported.  
### Description
Adds a new custom filter with a complete resolver.
<TData>: The type of the data that is filtered by the [QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).  
  
<TFilter>: The type of the data that is compared by the filter.  
  
Use this overload to register basic filters if you need to handle the operators yourself.
```
using System.Collections.Generic;
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_QueryEngine_AddFilter_Resolver
{
    static List<MyObjectType> s_Data;

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)/AddFilter_Resolver")]
    public static void RunExample()
    {
        // Set up the query engine
        var queryEngine = new QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType>();
        queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });

        // Add a custom filter "is", with a resolver that will handle all operators
        queryEngine.AddFilter<string>("is", (myObj, operatorToken, filterValue) =>
        {
            if (operatorToken != ":")
                return false;

            switch (filterValue)
            {
                case "active":
                    return myObj.active;
                case "root":
                    return myObj.id == 0;
                case "center":
                    return myObj.position == Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html);
                default: return false;
            }
        }, new[] {":"});

        s_Data = new List<MyObjectType>()
        {
            new MyObjectType { id = 0, name = "Test 1", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 0), active = false },
            new MyObjectType { id = 1, name = "Test 2", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 1), active = true },
            new MyObjectType { id = 2, name = "Test 3", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1, 0), active = false },
            new MyObjectType { id = 3, name = "Test 4", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(1.2f, 0), active = false },
        };

        // Find all items that are of type "active"
        var query = queryEngine.ParseQuery("is:active");
        var filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[1]), "Test 2 should be in the list as it is active.");

        // Find all items that are root
        query = queryEngine.ParseQuery("is:root");
        filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[0]), "Test 1 should be in the list as it is a root.");
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
## Declaration
public void AddFilter(string token, Func<TData,TParam,string,TFilter,bool> filterResolver, string[] supportedOperatorType); 
## Declaration
public void AddFilter(string token, Func<TData,TParam,string,TFilter,bool> filterResolver, Func<string,TParam> parameterTransformer, string[] supportedOperatorType); 
### Parameters
Parameter | Description  
---|---  
token | The identifier of the filter. Typically what precedes the operator in a filter (for example, "id" in "id>=2").  
filterResolver | Callback used to handle any operators for this filter. Takes an object of type TData, an object of type TParam, the operator token and the filter value, and returns a boolean indicating if the filter passed or not.  
parameterTransformer | Callback used to convert a string to type TParam. Used when parsing the query to convert what is passed to the function into the correct format.  
supportedOperatorType | List of supported operator tokens. This list contains the supported operator tokens. Use null or an empty list to indicate that all operators are supported.  
### Description
Adds a new custom filter with parameters and a complete resolver.
<TData>: The type of the data that is filtered by the [QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).  
  
<TFilter>: The type of the data that is compared by the filter.  
  
<TParam>: The type of the data that is passed to the filter.  
  
Use this overload to register filters that accept parameters if you need to handle the operators yourself.
```
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_QueryEngine_AddFilter_Param_Resolver
{
    static List<MyObjectType> s_Data;

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)/AddFilter_Param_Resolver")]
    public static void RunExample()
    {
        // Set up the query engine
        var queryEngine = new QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType>();
        queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });

        // Add a "dist" filter to filter items based on a specified distance from a position or from another item, and handle all operators
        queryEngine.AddFilter<Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html), string>("dist", (myObj, paramPosition, operatorToken, filterValue) =>
        {
            var distance = (myObj.position - paramPosition).magnitude;

            if (operatorToken == ":")
            {
                switch (filterValue)
                {
                    case "near":
                        return distance <= 10.0f;
                    case "far":
                        return distance > 10.0f;
                }
                return false;
            }

            var floatValue = float.Parse(filterValue, CultureInfo.InvariantCulture.NumberFormat);
            switch (operatorToken)
            {
                case "=":
                    return distance == floatValue;
                case "!=":
                    return distance != floatValue;
                case "<":
                    return distance < floatValue;
                case "<=":
                    return distance <= floatValue;
                case ">":
                    return distance > floatValue;
                case ">=":
                    return distance >= floatValue;
            }
            return false;
        }, paramStringValue =>
            {
                // Transform[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Transform.html) the parameter from a string to a usable Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)

                // If the user specified a vector
                if (paramStringValue.StartsWith("[") && paramStringValue.EndsWith("]"))
                {
                    paramStringValue = paramStringValue.Trim('[', ']');
                    var vectorTokens = paramStringValue.Split(',');
                    var vectorValues = vectorTokens.Select(token => float.Parse(token, CultureInfo.InvariantCulture.NumberFormat)).ToList();
                    return new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(vectorValues[0], vectorValues[1]);
                }

                // Treat the value as the name of an object
                var myObj = s_Data.Find(obj => obj.name == paramStringValue);
                return myObj.position;
            });

        s_Data = new List<MyObjectType>()
        {
            new MyObjectType { id = 0, name = "Test 1", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 0), active = false },
            new MyObjectType { id = 1, name = "Test 2", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(0, 10), active = true },
            new MyObjectType { id = 2, name = "Test 3", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(10, 0), active = false },
            new MyObjectType { id = 3, name = "Test 4", position = new Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html)(12f, 0), active = false },
        };

        // Find all items that are "near" "Test 1", including "Test 1"
        var query = queryEngine.ParseQuery("dist(Test 1):near");
        var filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 3, $"There should be 3 items in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(!filteredData.Contains(s_Data[3]), "Test 4 should not be in the list as it is far of Test 1.");

        // Find all items that are far of [0, 0]
        query = queryEngine.ParseQuery("dist([0, 0]):far");
        filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[3]), "Test 4 should be in the list as it is far of [0, 0].");
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
## Declaration
public [Search.IQueryEngineFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IQueryEngineFilter.html) AddFilter(Regex token, Func<TData,string,TFilter> getDataFunc, string[] supportedOperatorType); 
## Declaration
public [Search.IQueryEngineFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IQueryEngineFilter.html) AddFilter(Regex token, Func<TData,string,TFilter> getDataFunc, stringComparison stringComparison, string[] supportedOperatorType); 
### Parameters
Parameter | Description  
---|---  
token | The regular expression that matches the filter. Matches what precedes the operator in a filter (for example, "id" in "id>=2").  
getDataFunc | Callback used to get the object that is used in the filter. Takes an object of type TData, a string representing the actual filter name that was matched and returns an object of type TFilter.  
supportedOperatorType | List of supported operator tokens. This list contains the supported operator tokens. Use null or an empty list to indicate that all operators are supported.  
stringComparison | String comparison option.  
### Returns
**IQueryEngineFilter** The new filter. 
### Description
Adds a new custom filter with a regular expression.
<TData>: The type of the data that is filtered by the [QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).  
  
<TFilter>: The type of the data that is compared by the filter.  
  
Use this overload to register basic filters that match a regular expression if you don't need to handle the operators yourself.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_QueryEngine_AddFilter_Regex
{
    static List<MyObjectType> s_Data;

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)/AddFilter_Regex")]
    public static void RunExample()
    {
        // Set up the query engine
        var queryEngine = new QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType>();
        queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });
        SetupPropertyHandlers(queryEngine);

        // Add a regular expression filter to filter generic properties
        // When adding a new regular expression filter, there needs to be a single capturing group to retrieve the
        // actual name of the filter that matched.
        queryEngine.AddFilter(new Regex("#([\\w.]+)"), (myObj, filterNameMatch) =>
        {
            if (myObj.property.name == filterNameMatch)
                return myObj.property;
            return Property.invalid;
        });

        s_Data = new List<MyObjectType>()
        {
            new MyObjectType { id = 0, property = new Property("size", PropertyType.Integer, 64) },
            new MyObjectType { id = 1, property = new Property("size", PropertyType.Integer, 128) },
            new MyObjectType { id = 2, property = new Property("tag", PropertyType.String, "item") },
            new MyObjectType { id = 3, property = new Property("tag", PropertyType.String, "car item") }
        };

        // Find all objects that have a property "size" greater than 32
        var query = queryEngine.ParseQuery("#size>32");
        var filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 2, $"There should be 2 items in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[0]), "Object 0 should be in the list as its property \"size\" is > 32.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[1]), "Object 1 should be in the list as its property \"size\" is > 32.");

        // Find all objects that have a property "size" equal to 128
        query = queryEngine.ParseQuery("#size=128");
        filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[1]), "Object 1 should be in the list as its property \"size\" is = 128.");

        // Find all objects that have a property "tag" that contains "item"
        query = queryEngine.ParseQuery("#tag:item");
        filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 2, $"There should be 2 items in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[2]), "Object 2 should be in the list as its property \"tag\" contains \"item\".");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[3]), "Object 3 should be in the list as its property \"tag\" contains \"item\".");
    }

    static void SetupPropertyHandlers(QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType> qe)
    {
        qe.AddOperatorHandler(":", (Property v, int number, StringComparison sc) => PropertyIntCompare(v, number, (f, r) => f.ToString().IndexOf(r.ToString()) != -1));
        qe.AddOperatorHandler("=", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f == r));
        qe.AddOperatorHandler("!=", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f != r));
        qe.AddOperatorHandler("<=", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f <= r));
        qe.AddOperatorHandler("<", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f < r));
        qe.AddOperatorHandler(">", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f > r));
        qe.AddOperatorHandler(">=", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f >= r));
        qe.AddOperatorHandler(":", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => f.IndexOf(r, sc) != -1));
        qe.AddOperatorHandler("=", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Equals(f, r, sc)));
        qe.AddOperatorHandler("!=", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => !string.Equals(f, r, sc)));
        qe.AddOperatorHandler("<=", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Compare(f, r, sc) <= 0));
        qe.AddOperatorHandler("<", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Compare(f, r, sc) < 0));
        qe.AddOperatorHandler(">", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Compare(f, r, sc) > 0));
        qe.AddOperatorHandler(">=", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Compare(f, r, sc) >= 0));
    }

    static bool PropertyStringCompare(Property p, string s, Func<string, string, bool> comparer)
    {
        if (p.type != PropertyType.String)
            return false;
        return comparer((string)p.value, s);
    }

    static bool PropertyIntCompare(Property p, int number, Func<int, int, bool> comparer)
    {
        if (p.type != PropertyType.Integer)
            return false;
        return comparer((int)p.value, number);
    }

    enum PropertyType
    {
        None,
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

        public static Property invalid = new Property(string.Empty, PropertyType.None, null);
    }

    class MyObjectType
    {
        public int id { get; set; }
        public string name { get; set; } = string.Empty;
        public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position { get; set; } = Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html);
        public bool active { get; set; }
        public Property property { get; set; } = Property.invalid;

        public override string ToString()
        {
            return $"({id}, {name}, ({position.x}, {position.y}), {active})";
        }
    }
}

```

* * *
## Declaration
public [Search.IQueryEngineFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IQueryEngineFilter.html) AddFilter(Regex token, Func<TData,string,TParam,TFilter> getDataFunc, string[] supportedOperatorType); 
## Declaration
public [Search.IQueryEngineFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IQueryEngineFilter.html) AddFilter(Regex token, Func<TData,string,TParam,TFilter> getDataFunc, stringComparison stringComparison, string[] supportedOperatorType); 
## Declaration
public [Search.IQueryEngineFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IQueryEngineFilter.html) AddFilter(Regex token, Func<TData,string,TParam,TFilter> getDataFunc, Func<string,TParam> parameterTransformer, string[] supportedOperatorType); 
## Declaration
public [Search.IQueryEngineFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IQueryEngineFilter.html) AddFilter(Regex token, Func<TData,string,TParam,TFilter> getDataFunc, Func<string,TParam> parameterTransformer, stringComparison stringComparison, string[] supportedOperatorType); 
### Parameters
Parameter | Description  
---|---  
token | The regular expression that matches the filter. Matches what precedes the operator in a filter (for example, "id" in "id>=2").  
getDataFunc | Callback used to get the object that is used in the filter. Takes an object of type TData, a string representing the actual filter name that was matched, an object of type TParam, and returns an object of type TFilter.  
supportedOperatorType | List of supported operator tokens. This list contains the supported operator tokens. Use null or an empty list to indicate that all operators are supported.  
stringComparison | String comparison option.  
parameterTransformer | Callback used to convert a string to type TParam. Used when parsing the query to convert what is passed to the function into the correct format.  
### Returns
**IQueryEngineFilter** The new filter. 
### Description
Adds a new custom filter with a regular expression and parameters.
<TData>: The type of the data that is filtered by the [QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).  
  
<TFilter>: The type of the data that is compared by the filter.  
  
<TParam>: The type of the data that is passed to the filter.  
  
Use this overload to register filters that match a regular expression and accept parameters if you don't need to handle the operators yourself.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_QueryEngine_AddFilter_Param_Regex
{
    static List<MyObjectType> s_Data;

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)/AddFilter_Param_Regex")]
    public static void RunExample()
    {
        // Set up the query engine
        var queryEngine = new QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType>();
        queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });
        SetupPropertyHandlers(queryEngine);

        // Add a regular expression filter function to filter generic properties with parameters
        // When adding a new regular expression filter, there needs to be a single capturing group to retrieve the
        // actual name of the filter that matched.
        queryEngine.AddFilter<int, Property>(new Regex("\\$([\\w.]+)"), (myObj, filterNameMatch, param) =>
        {
            if (myObj.property.name != filterNameMatch)
                return Property.invalid;
            if (myObj.property.type != PropertyType.Integer_Array)
                return Property.invalid;
            if (!(myObj.property.value is int[] array))
                return Property.invalid;
            if (param < 0 || param >= array.Length)
                return Property.invalid;
            return new Property(myObj.property.name, PropertyType.Integer, array[param]);
        });

        s_Data = new List<MyObjectType>()
        {
            new MyObjectType { id = 0, property = new Property("size", PropertyType.Integer, 64) },
            new MyObjectType { id = 1, property = new Property("size", PropertyType.Integer, 128) },
            new MyObjectType { id = 2, property = new Property("tag", PropertyType.String, "item") },
            new MyObjectType { id = 3, property = new Property("tag", PropertyType.String, "car item") },
            new MyObjectType { id = 4, property = new Property("values", PropertyType.Integer_Array, new int[] {0, 2, 42}) },
            new MyObjectType { id = 5, property = new Property("values", PropertyType.Integer_Array, new int[] {8, 52, 210}) },
            new MyObjectType { id = 6, property = new Property("weights", PropertyType.Integer_Array, new int[] {1000, 250, 400}) }
        };

        // Find all objects that have a property "values" with a sub value greater than 42 at index 1
        var query = queryEngine.ParseQuery("$values(1)>42");
        var filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[5]), "Object 5 should be in the list as its property \"values\" at index 1 is > 42.");

        // Find all objects that have a property "weights" with a sub value lower or equal to 1000 at index 0
        query = queryEngine.ParseQuery("$weights(0)<=1000");
        filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[6]), "Object 6 should be in the list as its property \"weights\" at index 0 is <= 1000.");
    }

    static void SetupPropertyHandlers(QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType> qe)
    {
        qe.AddOperatorHandler(":", (Property v, int number, StringComparison sc) => PropertyIntCompare(v, number, (f, r) => f.ToString().IndexOf(r.ToString()) != -1));
        qe.AddOperatorHandler("=", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f == r));
        qe.AddOperatorHandler("!=", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f != r));
        qe.AddOperatorHandler("<=", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f <= r));
        qe.AddOperatorHandler("<", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f < r));
        qe.AddOperatorHandler(">", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f > r));
        qe.AddOperatorHandler(">=", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f >= r));
        qe.AddOperatorHandler(":", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => f.IndexOf(r, sc) != -1));
        qe.AddOperatorHandler("=", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Equals(f, r, sc)));
        qe.AddOperatorHandler("!=", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => !string.Equals(f, r, sc)));
        qe.AddOperatorHandler("<=", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Compare(f, r, sc) <= 0));
        qe.AddOperatorHandler("<", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Compare(f, r, sc) < 0));
        qe.AddOperatorHandler(">", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Compare(f, r, sc) > 0));
        qe.AddOperatorHandler(">=", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Compare(f, r, sc) >= 0));
    }

    static bool PropertyStringCompare(Property p, string s, Func<string, string, bool> comparer)
    {
        if (p.type != PropertyType.String)
            return false;
        return comparer((string)p.value, s);
    }

    static bool PropertyIntCompare(Property p, int number, Func<int, int, bool> comparer)
    {
        if (p.type != PropertyType.Integer)
            return false;
        return comparer((int)p.value, number);
    }

    enum PropertyType
    {
        None,
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

        public static Property invalid = new Property(string.Empty, PropertyType.None, null);
    }

    class MyObjectType
    {
        public int id { get; set; }
        public string name { get; set; } = string.Empty;
        public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position { get; set; } = Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html);
        public bool active { get; set; }
        public Property property { get; set; } = Property.invalid;

        public override string ToString()
        {
            return $"({id}, {name}, ({position.x}, {position.y}), {active})";
        }
    }
}

```

* * *
## Declaration
public [Search.IQueryEngineFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IQueryEngineFilter.html) AddFilter(Regex token, Func<TData,string,string,TFilter,bool> filterResolver, string[] supportedOperatorType); 
### Parameters
Parameter | Description  
---|---  
token | The regular expression that matches the filter. Matches what precedes the operator in a filter (for example, "id" in "id>=2").  
filterResolver | Callback used to handle any operators for this filter. Takes an object of type TData, a string representing the actual filter name that was matched, the operator token and the filter value, and returns a boolean indicating if the filter passed or not.  
supportedOperatorType | List of supported operator tokens. This list contains the supported operator tokens. Use null or an empty list to indicate that all operators are supported.  
### Returns
**IQueryEngineFilter** The new filter. 
### Description
Adds a new custom filter with a regular expression and a complete resolver.
<TData>: The type of the data that is filtered by the [QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).  
  
<TFilter>: The type of the data that is compared by the filter.  
  
Use this overload to register basic filters that match a regular expression if you need to handle the operators yourself.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using System.Linq;
using System.Text.RegularExpressions;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_QueryEngine_AddFilter_Resolver_Regex
{
    static List<MyObjectType> s_Data;

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)/AddFilter_Resolver_Regex")]
    public static void RunExample()
    {
        // Set up the query engine
        var queryEngine = new QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType>();
        queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });
        SetupPropertyHandlers(queryEngine);

        // Add a regular expression filter to filter generic properties, with a resolver to handle all operators yourself.
        // When adding a new regular expression filter, there needs to be a single capturing group to retrieve the
        // actual name of the filter that matched.
        queryEngine.AddFilter<string>(new Regex("p_([\\w]+)"), (myObj, filterNameMatch, operatorToken, filterValue) =>
        {
            if (operatorToken != ":")
                return false;
            if (myObj.property.name != filterNameMatch)
                return false;

            switch (filterValue)
            {
                case "enabled":
                    return myObj.property.enabled;
                case "empty":
                    {
                        if (myObj.property.type != PropertyType.Integer_Array)
                            return false;
                        if (!(myObj.property.value is int[] array))
                            return false;
                        return array.Length == 0;
                    }
                default: return false;
            }
        }, new[] {":"});

        s_Data = new List<MyObjectType>()
        {
            new MyObjectType { id = 0, property = new Property("size", PropertyType.Integer, 64, true) },
            new MyObjectType { id = 1, property = new Property("size", PropertyType.Integer, 128, false) },
            new MyObjectType { id = 2, property = new Property("tag", PropertyType.String, "item", true) },
            new MyObjectType { id = 3, property = new Property("tag", PropertyType.String, "car item", false) },
            new MyObjectType { id = 4, property = new Property("values", PropertyType.Integer_Array, new int[] {0, 2, 42}, true) },
            new MyObjectType { id = 5, property = new Property("values", PropertyType.Integer_Array, new int[] {8, 52, 210}, false) },
            new MyObjectType { id = 6, property = new Property("weights", PropertyType.Integer_Array, new int[] {1000, 250, 400}, false) },
            new MyObjectType { id = 7, property = new Property("weights", PropertyType.Integer_Array, new int[] {}, false) }
        };

        // Find all items that have a property "size" that is enabled.
        var query = queryEngine.ParseQuery("p_size:enabled");
        var filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[0]), "Object 0 should be in the list as its property \"size\" is enabled.");

        // Find all items that have a property "weights" that is empty.
        query = queryEngine.ParseQuery("p_weights:empty");
        filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[7]), "Object 7 should be in the list as its property \"weights\" is empty.");
    }

    static void SetupPropertyHandlers(QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType> qe)
    {
        qe.AddOperatorHandler(":", (Property v, int number, StringComparison sc) => PropertyIntCompare(v, number, (f, r) => f.ToString().IndexOf(r.ToString()) != -1));
        qe.AddOperatorHandler("=", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f == r));
        qe.AddOperatorHandler("!=", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f != r));
        qe.AddOperatorHandler("<=", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f <= r));
        qe.AddOperatorHandler("<", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f < r));
        qe.AddOperatorHandler(">", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f > r));
        qe.AddOperatorHandler(">=", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f >= r));
        qe.AddOperatorHandler(":", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => f.IndexOf(r, sc) != -1));
        qe.AddOperatorHandler("=", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Equals(f, r, sc)));
        qe.AddOperatorHandler("!=", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => !string.Equals(f, r, sc)));
        qe.AddOperatorHandler("<=", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Compare(f, r, sc) <= 0));
        qe.AddOperatorHandler("<", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Compare(f, r, sc) < 0));
        qe.AddOperatorHandler(">", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Compare(f, r, sc) > 0));
        qe.AddOperatorHandler(">=", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Compare(f, r, sc) >= 0));
    }

    static bool PropertyStringCompare(Property p, string s, Func<string, string, bool> comparer)
    {
        if (p.type != PropertyType.String)
            return false;
        return comparer((string)p.value, s);
    }

    static bool PropertyIntCompare(Property p, int number, Func<int, int, bool> comparer)
    {
        if (p.type != PropertyType.Integer)
            return false;
        return comparer((int)p.value, number);
    }

    enum PropertyType
    {
        None,
        Integer,
        String,
        Integer_Array
    }

    struct Property
    {
        public string name { get; }
        public PropertyType type { get; }
        public object value { get; set; }
        public bool enabled { get; set; }

        public Property(string name, PropertyType type, object value, bool enabled)
        {
            this.name = name;
            this.type = type;
            this.value = value;
            this.enabled = enabled;
        }

        public static Property invalid = new Property(string.Empty, PropertyType.None, null, false);
    }

    class MyObjectType
    {
        public int id { get; set; }
        public string name { get; set; } = string.Empty;
        public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position { get; set; } = Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html);
        public bool active { get; set; }
        public Property property { get; set; } = Property.invalid;

        public override string ToString()
        {
            return $"({id}, {name}, ({position.x}, {position.y}), {active})";
        }
    }
}

```

* * *
## Declaration
public [Search.IQueryEngineFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IQueryEngineFilter.html) AddFilter(Regex token, Func<TData,string,TParam,string,TFilter,bool> filterResolver, string[] supportedOperatorType); 
## Declaration
public [Search.IQueryEngineFilter](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.IQueryEngineFilter.html) AddFilter(Regex token, Func<TData,string,TParam,string,TFilter,bool> filterResolver, Func<string,TParam> parameterTransformer, string[] supportedOperatorType); 
### Parameters
Parameter | Description  
---|---  
token | The regular expression that matches the filter. Matches what precedes the operator in a filter (for example, "id" in "id>=2").  
filterResolver | Callback used to handle any operators for this filter. Takes an object of type TData, a string representing the actual filter name that was matched, an object of type TParam, the operator token and the filter value, and returns a boolean indicating if the filter passed or not.  
supportedOperatorType | List of supported operator tokens. This list contains the supported operator tokens. Use null or an empty list to indicate that all operators are supported.  
parameterTransformer | Callback used to convert a string to type TParam. Used when parsing the query to convert what is passed to the function into the correct format.  
### Returns
**IQueryEngineFilter** The new filter. 
### Description
Adds a new custom filter with a regular expression, parameters and a complete resolver.
<TData>: The type of the data that is filtered by the [QueryEngine](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.html).  
  
<TFilter>: The type of the data that is compared by the filter.  
  
<TParam>: The type of the data that is passed to the filter.  
  
Use this overload to register filters that match a regular expression and accept parameters if you need to handle the operators yourself.
```
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);
using System.Collections.Generic;
using System.Globalization;
using System.Linq;
using System.Text.RegularExpressions;
using UnityEditor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEditor.html);
using UnityEditor.Search;
using UnityEngine;

static class Example_QueryEngine_AddFilter_Param_Resolver_Regex
{
    static List<MyObjectType> s_Data;

    [MenuItem[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MenuItem.html)("Examples/QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)/AddFilter_Param_Resolver_Regex")]
    public static void RunExample()
    {
        // Set up the query engine
        var queryEngine = new QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType>();
        queryEngine.SetSearchDataCallback(myObj => new[] { myObj.id.ToString(), myObj.name });

        // Add a regular expression filter to filter generic properties, with a resolver to handle all operators yourself.
        // When adding a new regular expression filter, there needs to be a single capturing group to retrieve the
        // actual name of the filter that matched.
        queryEngine.AddFilter<int, string>(new Regex("p_([\\w]+)"), (myObj, filterNameMatch, index, operatorToken, filterValue) =>
        {
            if (myObj.property.name != filterNameMatch)
                return false;
            if (myObj.property.type != PropertyType.Integer_Array)
                return false;
            if (!(myObj.property.value is int[] array))
                return false;

            if (operatorToken == ":")
            {
                switch (filterValue)
                {
                    case "valid":
                        return index >= 0 && index < array.Length;
                    default: return false;
                }
            }

            if (index < 0 || index >= array.Length)
                return false;

            var value = array[index];
            var integerValue = int.Parse(filterValue, CultureInfo.InvariantCulture.NumberFormat);
            switch (operatorToken)
            {
                case "=":
                    return value == integerValue;
                case "!=":
                    return value != integerValue;
                case "<":
                    return value < integerValue;
                case "<=":
                    return value <= integerValue;
                case ">":
                    return value > integerValue;
                case ">=":
                    return value >= integerValue;
            }
            return false;
        });

        s_Data = new List<MyObjectType>()
        {
            new MyObjectType { id = 0, property = new Property("size", PropertyType.Integer, 64, true) },
            new MyObjectType { id = 1, property = new Property("size", PropertyType.Integer, 128, false) },
            new MyObjectType { id = 2, property = new Property("tag", PropertyType.String, "item", true) },
            new MyObjectType { id = 3, property = new Property("tag", PropertyType.String, "car item", false) },
            new MyObjectType { id = 4, property = new Property("values", PropertyType.Integer_Array, new int[] {0, 2, 42}, true) },
            new MyObjectType { id = 5, property = new Property("values", PropertyType.Integer_Array, new int[] {8, 52, 210}, false) },
            new MyObjectType { id = 6, property = new Property("weights", PropertyType.Integer_Array, new int[] {1000, 250, 400}, false) },
            new MyObjectType { id = 7, property = new Property("weights", PropertyType.Integer_Array, new int[] {}, false) }
        };

        // Find all items that have a property named "weights" with a valid value at index 2.
        var query = queryEngine.ParseQuery("p_weights(2):valid");
        var filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[6]), "Object 6 should be in the list as its property \"weights\" has a valid value at index 2.");

        // Find all items that have a property named "values" with a value greater than 50 at index 1.
        query = queryEngine.ParseQuery("p_values(1)>50");
        filteredData = query.Apply(s_Data).ToList();
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Count == 1, $"There should be 1 item in the filtered list but found {filteredData.Count} items.");
        Debug.Assert[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Assert.html)(filteredData.Contains(s_Data[5]), "Object 5 should be in the list as its property \"values\" has a value > 50 at index 1.");
    }

    static void SetupPropertyHandlers(QueryEngine[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine.html)<MyObjectType> qe)
    {
        qe.AddOperatorHandler(":", (Property v, int number, StringComparison sc) => PropertyIntCompare(v, number, (f, r) => f.ToString().IndexOf(r.ToString()) != -1));
        qe.AddOperatorHandler("=", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f == r));
        qe.AddOperatorHandler("!=", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f != r));
        qe.AddOperatorHandler("<=", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f <= r));
        qe.AddOperatorHandler("<", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f < r));
        qe.AddOperatorHandler(">", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f > r));
        qe.AddOperatorHandler(">=", (Property v, int number) => PropertyIntCompare(v, number, (f, r) => f >= r));
        qe.AddOperatorHandler(":", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => f.IndexOf(r, sc) != -1));
        qe.AddOperatorHandler("=", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Equals(f, r, sc)));
        qe.AddOperatorHandler("!=", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => !string.Equals(f, r, sc)));
        qe.AddOperatorHandler("<=", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Compare(f, r, sc) <= 0));
        qe.AddOperatorHandler("<", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Compare(f, r, sc) < 0));
        qe.AddOperatorHandler(">", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Compare(f, r, sc) > 0));
        qe.AddOperatorHandler(">=", (Property v, string s, StringComparison sc) => PropertyStringCompare(v, s, (f, r) => string.Compare(f, r, sc) >= 0));
    }

    static bool PropertyStringCompare(Property p, string s, Func<string, string, bool> comparer)
    {
        if (p.type != PropertyType.String)
            return false;
        return comparer((string)p.value, s);
    }

    static bool PropertyIntCompare(Property p, int number, Func<int, int, bool> comparer)
    {
        if (p.type != PropertyType.Integer)
            return false;
        return comparer((int)p.value, number);
    }

    enum PropertyType
    {
        None,
        Integer,
        String,
        Integer_Array
    }

    struct Property
    {
        public string name { get; }
        public PropertyType type { get; }
        public object value { get; set; }
        public bool enabled { get; set; }

        public Property(string name, PropertyType type, object value, bool enabled)
        {
            this.name = name;
            this.type = type;
            this.value = value;
            this.enabled = enabled;
        }

        public static Property invalid = new Property(string.Empty, PropertyType.None, null, false);
    }

    class MyObjectType
    {
        public int id { get; set; }
        public string name { get; set; } = string.Empty;
        public Vector2[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2.html) position { get; set; } = Vector2.zero[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector2-zero.html);
        public bool active { get; set; }
        public Property property { get; set; } = Property.invalid;

        public override string ToString()
        {
            return $"({id}, {name}, ({position.x}, {position.y}), {active})";
        }
    }
}

```

* * *
