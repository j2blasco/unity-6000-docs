* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.SetBoundingSphereCount.html

#  [CullingGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.html).SetBoundingSphereCount
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
public void SetBoundingSphereCount(int count); 
### Parameters
Parameter | Description  
---|---  
count | The number of bounding spheres being used.  
### Description
Sets the number of bounding spheres in the bounding spheres array that are actually being used.
For performance reasons, you should not repeatedly re-allocate your bounding spheres array as new spheres are added and removed; instead you should create one array at the maximum size you will need, and then track the number of spheres that are actually being used within it. This way you avoid expensive allocation and copy operations.
* * *
