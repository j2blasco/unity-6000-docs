* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.SetBoundingDistances.html

#  [CullingGroup](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.html).SetBoundingDistances
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
public void SetBoundingDistances(float[] distances); 
### Parameters
Parameter | Description  
---|---  
distances | An array of bounding distances. The distances should be sorted in increasing order.  
### Description
Set bounding distances for 'distance bands' the group should compute, as well as options for how spheres falling into each distance band should be treated.
Each distance value indicates a band that is 'up to' that distance; the array [10, 20, 30] describes distance bands "from 0 to 10m", "from 10m to 20m" and "from 20m to 30m."  
  
The distance from the reference point (set by [CullingGroup.SetDistanceReferencePoint](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.SetDistanceReferencePoint.html)) to the nearest edge of the sphere is used to calculate which distance band a sphere is in. Therefore a sphere that covers multiple distance bands will be considered to be in the nearest one to the reference point.  
  
In addition to forcing objects to be visible or invisible, you can use distance bands to drive level-of-detail changes in your objects. For example, you might define bands "from 0 to 40m" and "from 40m to 80m", and while you might have both bands apply occlusion and frustum culling as normal, you could have objects in the second band be animated with a less complex rig, or run a less complex AI behaviour.  
  
By default, any spheres beyond the final bounding distance are implicitly forced to be invisible. To avoid this, you can specify a final bounding distance of float.PositiveInfinity.
* * *
