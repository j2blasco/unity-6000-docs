* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth-stiffnessFrequency.html

#  [Cloth](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Cloth.html).stiffnessFrequency
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
stiffnessFrequency; 
### Description
Sets the stiffness frequency parameter.
The stiffness frequency controls the power-law nonlinearity of all rate of change parameters (stretch stiffness, shear stiffness, bending stiffness, tether stiffness, self-collision stiffness, motion constraint stiffness, damp coefficient, linear and angular drag coefficients). Increasing the frequency avoids numerical cancellation for values near zero or one, but increases the non-linearity of the parameter. It is not recommended to change this parameter after cloth initialization. For example, the portion of edge overstretch removed per second is equal to the stretch stiffness raised to the power of the stiffness frequency.
* * *
