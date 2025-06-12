* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.SelectIfAttribute-ctor.html

# SelectIfAttribute Constructor
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
public SelectIfAttribute(object condition, bool overridePriority, string filePath, int lineNumber, params string[] keywordNames); 
### Parameters
Parameter | Description  
---|---  
condition | Unity compares the data field to this value. The outcome determines the filter behavior.  
overridePriority | Whether this filter attribute overrides filter attributes that are already active on the same keywords. The default is `false`.  
filePath | The path of the file this attribute is in. Automatically filled by default.  
lineNumber | The line number of this attribute. Automatically filled by default.  
keywordNames | An array of shader keyword names the filter attribute will apply to.  
### Description
Include only the specified shader keywords in the build if the data field matches the condition.
Additional resources: [FilterAttribute](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.FilterAttribute.html).
* * *
