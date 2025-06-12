* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngineFilterAttribute.html

# QueryEngineFilterAttribute
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
Base attribute class used to define a custom filter on a QueryEngine. All filter types supported by QueryEngine.AddFilter are supported by this attribute.
For a usage example, see [QueryEngine.AddFiltersFromAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngine_1.AddFiltersFromAttribute.html).
### Properties
Property | Description  
---|---  
[comparisonOptions](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngineFilterAttribute-comparisonOptions.html) | String comparison options.  
[overridesStringComparison](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngineFilterAttribute-overridesStringComparison.html) | Flag indicating if the filter overrides the global string comparison options. Set to true when the comparisonOptions are used.  
[paramTransformerFunction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngineFilterAttribute-paramTransformerFunction.html) | Name of the parameter transformer function to use with this filter. Tag the parameter transformer function with the appropriate ParameterTransformer attribute.  
[supportedOperators](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngineFilterAttribute-supportedOperators.html) | List of supported operator tokens. Null for all operators.  
[token](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngineFilterAttribute-token.html) | The identifier of the filter. Typically what precedes the operator in a filter (i.e. "id" in "id>=2").  
[useParamTransformer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngineFilterAttribute-useParamTransformer.html) | Flag indicating if this filter uses a parameter transformer function. Set to true when paramTransformerFunction is used.  
[useRegularExpressionToken](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngineFilterAttribute-useRegularExpressionToken.html) | Indicates if the filter uses a regular expression token or not.  
### Constructors
Constructor | Description  
---|---  
[QueryEngineFilterAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.QueryEngineFilterAttribute-ctor.html) | Create a filter with the corresponding token and supported operators.  
* * *
