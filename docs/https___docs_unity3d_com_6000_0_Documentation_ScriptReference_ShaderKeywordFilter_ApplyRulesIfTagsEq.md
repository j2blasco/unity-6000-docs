* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.ApplyRulesIfTagsEqualAttribute-ctor.html

# ApplyRulesIfTagsEqualAttribute Constructor
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
public ApplyRulesIfTagsEqualAttribute(params string[] tags); 
### Parameters
Parameter | Description  
---|---  
tags | An array of strings with tag names and values. Use the first element in the array for the tag name, then the second element for the tag value, and so on.  
### Description
Enable or disable shader keyword filter attributes based on shader tags.
Unity enables filter attributes if the shader compilation context contains any of the tags.
* * *
