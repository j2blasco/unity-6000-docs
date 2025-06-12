* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ShaderKeywordFilter.TagConstraintAttribute-ctor.html

# TagConstraintAttribute Constructor
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
public TagConstraintAttribute(bool negate, params string[] tags); 
### Parameters
Parameter | Description  
---|---  
negate | Set to `true` to enable filter attributes when shader tags do not match any of the `tags`.  
tags | The array of tag name-value pairs to match to.  
### Description
Enable or disable shader keyword filter attributes based on shader tags.
Unity enables filter attributes if the shader compilation context contains any of the tags.
* * *
