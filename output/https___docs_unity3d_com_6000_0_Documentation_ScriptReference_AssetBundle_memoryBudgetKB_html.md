* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle-memoryBudgetKB.html

#  [AssetBundle](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.html).memoryBudgetKB
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
memoryBudgetKB; 
### Description
Controls the size of the shared AssetBundle loading cache. Default value is 1MB. 
Depending on your AssetBundle build and load strategy, sections of the AssetBundle file may be accessed multiple times. To improve loading performance, the AssetBundle loading cache stores recently accessed pages of the AssetBundle file. The default cache size should be sufficient in most cases, but the optimal cache size may vary depending on your workload. The optimal size can be determined by measuring how different cache sizes affect the AssetBundle loading times of your specific workload. If you load lots of small objects (e.g. 100 addressable prefabs) individually out of an AssetBundle, a larger cache would likely improve performance since future reads of other objects might reuse cached pages. If your AssetBundle consists of fewer large objects, or if you read all your objects simultaneously with functions like [AssetBundle.LoadAll](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/AssetBundle.LoadAll.html), a larger cache may not help since the cached pages will likely not be revisited.
* * *
