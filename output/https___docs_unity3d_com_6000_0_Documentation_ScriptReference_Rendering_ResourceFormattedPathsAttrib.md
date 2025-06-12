* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.ResourceFormattedPathsAttribute-ctor.html

# ResourceFormattedPathsAttribute Constructor
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
public ResourceFormattedPathsAttribute(string pathFormat, int rangeMin, int rangeMax, [Rendering.SearchType](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.SearchType.html) location); 
### Parameters
Parameter | Description  
---|---  
pathFormat | The format used for the path with a varying index.  
rangeMin | The varying index start value (included)  
rangeMax | The varying index end value (excluded)  
location | Specify if the given paths are from the builtin, builtinExtra or project resources.  
### Description
Creates a new ResourceFormattedPathsAttribute for an array's elements using formatted path names.
* * *
