* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.Providers.SceneQueryEngineFilterAttribute-ctor.html

# SceneQueryEngineFilterAttribute Constructor
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
public SceneQueryEngineFilterAttribute(string token, string[] supportedOperators); 
## Declaration
public SceneQueryEngineFilterAttribute(string token, stringComparison options, string[] supportedOperators); 
## Declaration
public SceneQueryEngineFilterAttribute(string token, string paramTransformerFunction, string[] supportedOperators); 
## Declaration
public SceneQueryEngineFilterAttribute(string token, string paramTransformerFunction, stringComparison options, string[] supportedOperators); 
### Parameters
Parameter | Description  
---|---  
token | The identifier of the filter. Typically what precedes the operator in a filter (i.e. "id" in "id>=2").  
supportedOperators | List of supported operator tokens. Null for all operators.  
options | String comparison options.  
paramTransformerFunction | Name of the parameter transformer function to use with this filter. Tag the parameter transformer function with the appropriate ParameterTransformer attribute. See [SceneQueryEngineParameterTransformer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.Providers.SceneQueryEngineParameterTransformerAttribute.html) for more information.  
### Description
Create a filter with the corresponding token and supported operators.
The following example adds a new filter function `dist` that returns the distance between an object and a point. This filter needs a parameter [transformer](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Search.Providers.SceneQueryEngineParameterTransformerAttribute.html) to transform the text into a point. Also, it doesn't support the operator "contains" (`:`).
```
[SceneQueryEngineFilter("dist", "DistanceParamHandler", new[] {"=", "!=", "<", ">", "<=", ">="})]
static float DistanceHandler(GameObject[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.html) go, Vector3[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) p)
{
    return (go.transform.position - p).magnitude;
}

```

* * *
