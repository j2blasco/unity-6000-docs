* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationJacobian.html

# ArticulationJacobian
struct in UnityEngine
/
Implemented in:[UnityEngine.PhysicsModule](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/UnityEngine.PhysicsModule.html)
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
The floating point dense Jacobian matrix of the articulation body hierarchy.
Jacobian matrix is important concept used in robotics and inverse kinematics. Multiplication with the Jacobian matrix maps the reduced coordinate space joint velocities of the articulated body to world space velocities. Also can be used for inverse kinematics, because it can provide relation between joint velocities and end effector velocities of the articulated body. Additional resources: [ArticulationBody.GetDenseJacobian](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetDenseJacobian.html). 
### Properties
Property | Description  
---|---  
[columns](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationJacobian-columns.html) | Number of columns of the matrix is equal to the total number of all joint degrees of freedom(DOF), plus 6 if ArticulationBody.immovable is false.  
[elements](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationJacobian-elements.html) | List of floats representing Jacobian matrix.  
[rows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationJacobian-rows.html) | Number of rows of the matrix is equal to the number of articulation bodies in hierarchy times 6: 3 rows of linear/positional DOF and 3 rows of angular/rotational DOF for each body.  
[this[int,int]](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationJacobian.Index_operator.html) | Gets the [row, col] element of the matrix.  
### Constructors
Constructor | Description  
---|---  
[ArticulationJacobian](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationJacobian-ctor.html) | Initializes nRows X nCols Jacobian matrix to zeroes.  
* * *
