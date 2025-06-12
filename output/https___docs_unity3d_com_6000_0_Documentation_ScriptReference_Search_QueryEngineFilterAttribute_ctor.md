* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngineFilterAttribute-ctor.html

# QueryEngineFilterAttribute Constructor
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
public QueryEngineFilterAttribute(string token, string[] supportedOperators); 
## Declaration
public QueryEngineFilterAttribute(string token, stringComparison options, string[] supportedOperators); 
## Declaration
public QueryEngineFilterAttribute(string token, string paramTransformerFunction, string[] supportedOperators); 
## Declaration
public QueryEngineFilterAttribute(string token, string paramTransformerFunction, stringComparison options, string[] supportedOperators); 
### Parameters
Parameter | Description  
---|---  
token | The identifier of the filter. Typically what precedes the operator in a filter (for example, "id" in "id>=2").  
supportedOperators | List of supported operator tokens. This list contains the supported operator tokens. Use null or an empty list to indicate that all operators are supported.  
options | String comparison options.  
paramTransformerFunction | Name of the parameter transformer function to use with this filter. Tag the parameter transformer function with the appropriate ParameterTransformer attribute.  
### Description
Create a filter with the corresponding token and supported operators.
* * *
## Declaration
public QueryEngineFilterAttribute(string token, bool useRegularExpression, string[] supportedOperators); 
## Declaration
public QueryEngineFilterAttribute(string token, bool useRegularExpression, stringComparison options, string[] supportedOperators); 
## Declaration
public QueryEngineFilterAttribute(string token, bool useRegularExpression, string paramTransformerFunction, string[] supportedOperators); 
## Declaration
public QueryEngineFilterAttribute(string token, bool useRegularExpression, string paramTransformerFunction, stringComparison options, string[] supportedOperators); 
### Parameters
Parameter | Description  
---|---  
token | The identifier of the filter or regular expression that matches the filters. Typically what precedes the operator in a filter (for example, "id" in "id>=2").  
useRegularExpression | Set this flag to true if the token is a regular expression.  
supportedOperators | List of supported operator tokens. This list contains the supported operator tokens. Use null or an empty list to indicate that all operators are supported.  
options | String comparison options.  
paramTransformerFunction | Name of the parameter transformer function to use with this filter. Tag the parameter transformer function with the appropriate ParameterTransformer attribute.  
### Description
Create a filter with the corresponding token and supported operators.
This constructor allows custom filters with regular expressions to be registered with an attribute.
```
// Define a regular expression filter for the property "property".
[MyObjectFilter("#([\\w.]+)", true)]
static Property FilterProperty(MyObjectType myObj, string filterMatch)
{
    if (myObj.property.name == filterMatch)
        return myObj.property;
    return Property.invalid;
}

```

* * *
