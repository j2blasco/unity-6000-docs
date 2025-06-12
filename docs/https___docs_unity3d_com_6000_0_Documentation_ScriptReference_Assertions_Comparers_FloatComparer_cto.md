* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Comparers.FloatComparer-ctor.html

# FloatComparer Constructor
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
public FloatComparer(); 
## Declaration
public FloatComparer(bool relative); 
## Declaration
public FloatComparer(float error); 
## Declaration
public FloatComparer(float error, bool relative); 
### Parameters
Parameter | Description  
---|---  
relative | Should a relative check be used when comparing values? By default, an absolute check will be used.  
error | Allowed comparison error. By default, the [FloatComparer.kEpsilon](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Assertions.Comparers.FloatComparer-kEpsilon.html) is used.  
### Description
Creates an instance of the comparer.
* * *
