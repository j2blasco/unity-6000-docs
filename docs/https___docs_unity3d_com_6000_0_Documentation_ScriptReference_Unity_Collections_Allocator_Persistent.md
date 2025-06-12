* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Persistent.html

#  [Allocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.html).Persistent
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
Use a persistent allocation.
The slowest allocation but can last as long as you need it to, and if necessary, throughout the application's lifetime. It's a wrapper for a direct call to malloc. Longer jobs can use this NativeContainer allocation type. Don't use Persistent where performance is essential.
* * *
