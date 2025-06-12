* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.ClosestPointToPolyLine.html

#  [HandleUtility](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/HandleUtility.html).ClosestPointToPolyLine
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
public static [Vector3](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Vector3.html) ClosestPointToPolyLine(params Vector3[] vertices); 
### Description
Get the point on a polyline (in 3D space) which is closest to the current mouse position.
A polyline is simply a zigzag line defined by a set of points connected in sequence. The ClosestPointToPolyLine function takes the polyline defined by a point array and "flattens" it into screen space. The closest point between the flattened line and the current mouse position (also in screen space) is then found and converted back into a 3D point on the original 3D polyline. This is useful for Handle GUIs that involve manipulating an arbitrary 3D shape using the mouse; the 2D mouse movements are converted into 3D space in the familiar way used by Unity's built-in tools. An example of where this might be used is a racetrack defined by a set of waypoints - a position along the track line could be selected via the mouse using ClosestPointToPolyLine.
* * *
