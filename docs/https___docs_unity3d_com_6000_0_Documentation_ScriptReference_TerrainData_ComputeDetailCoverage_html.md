* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.ComputeDetailCoverage.html

#  [TerrainData](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TerrainData.html).ComputeDetailCoverage
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
public float ComputeDetailCoverage(int detailPrototypeIndex); 
### Description
This function computes and returns the coverage (how many instances fit in a square unit) of a detail prototype, given its index.
Computes detail coverage. In [CoverageMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DetailScatterMode.CoverageMode.html), this coverage represents the number of scattered instances per unit squared, based on the detail prototype's size and density settings. Unavailable in [InstanceCountMode](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/DetailScatterMode.InstanceCountMode.html).
* * *
