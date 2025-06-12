* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.TempJob.html

#  [Allocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.html).TempJob
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
Use a temporary job allocation.
A slower allocation than Temp but faster than Persistent. Use it for thread-safe allocations within a lifespan of four frames. **Important:** You must Dispose of this allocation type within four frames, or the console prints a warning, generated from the native code. Most small jobs use this allocation type.
* * *
