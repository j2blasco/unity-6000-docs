* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetDenseJacobian.html

#  [ArticulationBody](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.html).GetDenseJacobian
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
[Switch to Manual](https://docs.unity3d.com/6000.0/Documentation/Manual/class-ArticulationBody.html "Go to ArticulationBody Component in the Manual")
## Declaration
public int GetDenseJacobian(ref [ArticulationJacobian](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationJacobian.html) jacobian); 
### Parameters
Parameter | Description  
---|---  
jacobian | Supplied struct to read back and store Jacobian matrix values.   
### Returns
**int** Number of elements in Jacobian matrix. 
### Description
Calculates and writes dense Jacobian matrix of the articulation body hierarchy to the supplied struct.
This calculates dense Jacobian matrix of the entire articulation body hierarchy starting from root articulation body. Number of rows [ArticulationJacobian.rows](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationJacobian-rows.html) of the matrix is equal to the number of articulation bodies in hierarchy times 6: 3 rows of linear/positional DOF and 3 rows of angular/rotational DOF for each body. Number of columns [ArticulationJacobian.columns](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationJacobian-columns.html) of the matrix is equal to the total number of all joints degrees of freedom(DOF), plus 6 if [ArticulationBody.immovable](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-immovable.html) is false. Additional resources: [index](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody-index.html), [ArticulationJacobian](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationJacobian.html), [GetDofStartIndices](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/ArticulationBody.GetDofStartIndices.html). 
* * *
