* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLExceptionSupport.ExplicitlyThrownExceptionsOnly.html

#  [WebGLExceptionSupport](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLExceptionSupport.html).ExplicitlyThrownExceptionsOnly
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
Enable throw support.
With this option, exceptions can be thrown and caught in WebGL. But only exceptions explictly thrown will work. NullReferenceExceptions can still cause your content to fail. This has a significant cost in performance and build size over [WebGLExceptionSupport.None](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/WebGLExceptionSupport.None.html), so only use it when you need it.
* * *
