* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.FilterAttribute-ctor.html

# FilterAttribute Constructor
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
public FilterAttribute([ShaderKeywordFilter.FilterAction](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.FilterAction.html) action, [ShaderKeywordFilter.FilterAttribute.Precedence](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.FilterAttribute.Precedence.html) precedence, [ShaderKeywordFilter.FilterAttribute.EvaluationMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.FilterAttribute.EvaluationMode.html) evaluationMode, object condition, string fileName, int lineNumber, params string[] keywordNames); 
### Parameters
Parameter | Description  
---|---  
action | The filter action this attribute triggers.  
precedence | The mode of precedence between this attribute and any attributes evaluated before this.  
evaluationMode | The condition evaluation mode that's used to decide whether the condition is expected to match or not.  
condition | The value that's being compared against the targeted data field. The comparison outcome determines the filter behavior.  
fileName | The path of the file this attribute is in. Automatically filled by default.  
lineNumber | The line number of this attribute. Automatically filled by default.  
keywordNames | An array of shader keyword names this filter attribute affects.  
### Description
Tell the shader system which shader keywords to include in or exclude from the build, based on the data field underneath.
* * *
