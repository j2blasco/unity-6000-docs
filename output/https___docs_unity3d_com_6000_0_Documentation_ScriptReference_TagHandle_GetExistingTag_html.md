* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TagHandle.GetExistingTag.html

#  [TagHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TagHandle.html).GetExistingTag
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
public static [TagHandle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TagHandle.html) GetExistingTag(string tagName); 
### Parameters
Parameter | Description  
---|---  
tagName | The name of the tag to get a handle to.  
### Returns
**TagHandle** A new TagHandle for the existing tag. 
### Description
Get a handle to a existing defined tag.
This method can only be used to get references to tags that were already defined. If you pass a tag name which is not already defined, it will throw an exception.  
  
Additional resources: [GameObject.CompareTag](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/GameObject.CompareTag.html).
* * *
