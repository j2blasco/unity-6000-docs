* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroupEvent-currentDistance.html

#  [CullingGroupEvent](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroupEvent.html).currentDistance
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
currentDistance; 
### Description
The current distance band index of the sphere, after the most recent culling pass.
Note that this value will range from 0 to the length of the distance array passed to [CullingGroup.SetBoundingDistances](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/CullingGroup.SetBoundingDistances.html) _inclusive_ , as each bounding distance in the array is an upper bound for that index.  
  
For example, given bounding distances [10, 20, 30], the first band (index 0) is spheres that are between 0 and 10 units away from the reference point, the second band (index 1) is spheres between 10 and 20 units away from the reference point, the third band (index 2) is spheres between 20 and 30 units from the reference point, and the implicit fourth band (index 3) is spheres beyond 30 units from the reference point.
* * *
