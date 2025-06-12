* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-vertices.html

#  [Cloth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.html).vertices
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-Cloth.html "Go to Cloth Component in the Manual")
vertices; 
### Description
The current vertex positions of the cloth object.
This gives you read access to the vertex positions of the cloth object, so you can analyse it's current simulation state. Note that the vertex indices may not necessarily correspond to the indices of the source mesh - especially when triangle stripping or UV seams are used in the source mesh (ie, multiple indices for the same vertex), cloth vertices will be different, as the cloth simulation only uses a single index for each vertex.
* * *
