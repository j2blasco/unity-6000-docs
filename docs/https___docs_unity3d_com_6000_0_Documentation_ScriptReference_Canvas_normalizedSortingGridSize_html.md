* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas-normalizedSortingGridSize.html

#  [Canvas](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Canvas.html).normalizedSortingGridSize
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
normalizedSortingGridSize; 
### Description
The normalized grid size that the canvas will split the renderable area into.
During rendering, the canvas splits the renderable area (bounds of all UI elements) into a grid. This is the normalized size of that grid. For example if you have a renderable area of 100 units with a sortingGridNormalizedSize of 0.1f then each grid cell would be 10 units.  
  
Note: a value of 0 will default to 0.1f.
* * *
