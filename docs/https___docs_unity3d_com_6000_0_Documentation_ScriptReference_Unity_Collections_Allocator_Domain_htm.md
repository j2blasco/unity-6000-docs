* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.Domain.html

#  [Allocator](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Unity.Collections.Allocator.html).Domain
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
Use an allocation associated with the lifetime of a domain.
You don't need to free this memory, because Unity frees it automatically at domain unload. However, to conserve memory, you can free it at any time. Freeing a large number of such allocations in one frame, such that the array of freed pointers is larger than L2 cache, might exhibit a measurable loss of performance.
* * *
