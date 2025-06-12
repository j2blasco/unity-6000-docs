* Source: https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.Coverage.GetStatsFor.html

#  [Coverage](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.Coverage.html).GetStatsFor
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
public static [TestTools.CoveredMethodStats](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.CoveredMethodStats.html) GetStatsFor(MethodBase method); 
### Parameters
Parameter | Description  
---|---  
method | The method to get coverage statistics for.  
### Returns
**CoveredMethodStats** Coverage summary. 
### Description
Returns the coverage summary for the specified method. See [CoveredMethodStats](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.CoveredMethodStats.html) for more information about the coverage statistics returned by this method.
```
using UnityEngine;
using UnityEngine.TestTools;
using System.Reflection;  
  
public class CoverageClass
{
    // A simple test method to get coverage information from.
    // If the method is called with incrementValue set to true,
    // the method will have complete coverage. If incrementValue
    // is false, the coverage will be incomplete.
    public int CoveredMethod(bool incrementValue)
    {
        int value = 0;
        if (incrementValue)
        {
            value++;
        }  
  
        return value;
    }
}  
  
public class CoverageExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Create an instance of the test class and call the test method
        // to make sure the method has had some coverage. Note in this example,
        // we're passing false into the method to make sure the coverage
        // is incomplete.
        CoverageClass coverageClasss = new CoverageClass();
        int value = coverageClasss.CoveredMethod(false);  
  
        // Use reflection to get the MethodBase for CoverageClass.CoveredMethod
        MethodBase coveredMethodBase = typeof(CoverageClass).GetMethod("CoveredMethod");
        // And get the coverage stats for the method.
        CoveredMethodStats[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.CoveredMethodStats.html) stats = Coverage.GetStatsFor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.Coverage.GetStatsFor.html)(coveredMethodBase);  
  
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("CoveredMethod has " + stats.totalSequencePoints + " sequence points");
        int coveredSequencePoints = stats.totalSequencePoints - stats.uncoveredSequencePoints;
        Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("of which " + coveredSequencePoints + " were covered.");
    }
}

```

* * *
## Declaration
public static CoveredMethodStats[] GetStatsFor(MethodBase[] methods); 
### Parameters
Parameter | Description  
---|---  
methods | The array of methods.  
### Returns
**CoveredMethodStats[]** Array of coverage summaries. 
### Description
Returns an array of coverage summaries for the specified array of methods.
```
using UnityEngine;
using UnityEngine.TestTools;
using System.Reflection;
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);  
  
// A simple test class to get coverage information for.
public class CoverageClass
{
    public bool CoveredMethod1()
    {
        return true;
    }  
  
    public bool CoveredMethod2()
    {
        return false;
    }
}  
  
public class CoverageExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Create an instance of the test class and call the test methods
        // to make sure the class has had some coverage.
        CoverageClass coverageClasss = new CoverageClass();
        coverageClasss.CoveredMethod1();
        coverageClasss.CoveredMethod2();  
  
        // Get the Type of the CoverageClass
        Type coverageClassType = typeof(CoverageClass);  
  
        // Use reflection to get an array of MethodBases for the two methods
        // in CoverageClass.
        MethodBase[] coveredMethodBaseArray =
        {
            coverageClassType.GetMethod("CoveredMethod1"),
            coverageClassType.GetMethod("CoveredMethod2")
        };  
  
        // And get the coverage stats for the methods.
        CoveredMethodStats[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.CoveredMethodStats.html)[] stats = Coverage.GetStatsFor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.Coverage.GetStatsFor.html)(coveredMethodBaseArray);  
  
        for (int i = 0; i < stats.Length; i++)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Method Name: " + stats[i].method.ToString());
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Method has " + stats[i].totalSequencePoints + " sequence points");
            int coveredSequencePoints = stats[i].totalSequencePoints - stats[i].uncoveredSequencePoints;
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("of which " + coveredSequencePoints + " were covered.");
        }
    }
}

```

* * *
## Declaration
public static CoveredMethodStats[] GetStatsFor(Type type); 
### Parameters
Parameter | Description  
---|---  
type | The type.  
### Returns
**CoveredMethodStats[]** Array of coverage summaries. 
### Description
Returns an array of coverage summaries for the specified type.
```
using UnityEngine;
using UnityEngine.TestTools;
using System[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Rendering.VirtualTexturing.System.html);  
  
// A simple test class to get coverage information for.
public class CoverageClass
{
    public bool CoveredMethod1()
    {
        return true;
    }  
  
    public bool CoveredMethod2()
    {
        return false;
    }
}  
  
public class CoverageExample : MonoBehaviour[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/MonoBehaviour.html)
{
    void Start()
    {
        // Create an instance of the test class and call the test methods
        // to make sure the class has had some coverage.
        CoverageClass coverageClasss = new CoverageClass();
        coverageClasss.CoveredMethod1();
        coverageClasss.CoveredMethod2();  
  
        // Get the Type of the CoverageClass
        Type coverageClassType = typeof(CoverageClass);
        // And get the coverage stats for all of the methods of the type.
        // Note that this will include class's default constructor.
        CoveredMethodStats[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.CoveredMethodStats.html)[] stats = Coverage.GetStatsFor[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/TestTools.Coverage.GetStatsFor.html)(coverageClassType);  
  
        for (int i = 0; i < stats.Length; i++)
        {
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Method Name: " + stats[i].method.ToString());
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("Method has " + stats[i].totalSequencePoints + " sequence points");
            int coveredSequencePoints = stats[i].totalSequencePoints - stats[i].uncoveredSequencePoints;
            Debug.Log[](https://docs.unity3d.com/6000.0/Documentation/ScriptReference/Debug.Log.html)("of which " + coveredSequencePoints + " were covered.");
        }
    }
}

```

* * *
