* Source: https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/physical-camera-reference.html

  * [Working in Unity](https://docs.unity3d.com/6000.0/Documentation/Manual/working-in-unity.html)
  * [Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/Cameras.html)
  * [Cameras in URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/urp-cameras-landing.html)
  * [Camera Inspector windows reference for URP](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-components-reference-landing.html)
  * Physical Camera Inspector window reference for URP


[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html)
Camera Inspector window reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/cameras-birp.html)
Cameras in the Built-In Render Pipeline
# Physical Camera Inspector window reference for URP
The physical **camera** A component which creates an image of a particular viewpoint in your scene. The output is either drawn to the screen or captured as a texture. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/CamerasOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#Camera) properties enable the URP camera to simulate a real-world camera. These properties correspond to features of real-world cameras and work in the same way.
For more information about how to use some of these properties to create the camera effect you desire, refer to [Using Physical Cameras](https://docs.unity3d.com/6000.0/Documentation/Manual/PhysicalCameras.html).
**Note:** When the Physical Camera is in use, Unity calculates the Field of View with the following properties:
  * **Sensor Size**
  * **Focal Length**
  * **Shift**


The Physical Camera properties are split into the following sections:
  * [Camera Body](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/physical-camera-reference.html#camera-body)
  * [Lens](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/physical-camera-reference.html#lens)
  * [Aperture Shape](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/cameras/physical-camera-reference.html#aperture-shape)


## Camera Body
**Property** | **Description**  
---|---  
**Sensor Type** | Specify the real-world camera format you want the camera to simulate. When you choose a camera format, Unity sets the **Sensor Size** > **X** and **Y** properties to the correct values automatically.  
  
URP offers the following camera format presets:
  * **8mm** :
    * **X** : 4.8
    * **Y** : 3.5
  * **Super 8mm** :
    * **X** : 5.79
    * **Y** : 4.01
  * **16mm** :
    * **X** : 10.26
    * **Y** : 7.49
  * **Super 16mm** :
    * **X** : 12.522
    * **Y** : 7.417
  * **35mm 2-perf** :
    * **X** : 21.95
    * **Y** : 9.35
  * **35mm Academy** :
    * **X** : 21.946
    * **Y** : 16.002
  * **Super–35** :
    * **X** : 24.89
    * **Y** : 18.66
  * **35mm TV Projection** :
    * **X** : 20.726
    * **Y** : 15.545
  * **35mm Full Aperture** :
    * **X** : 24.892
    * **Y** : 18.669
  * **35mm 1.85 Projection** :
    * **X** : 20.955
    * **Y** : 11.328
  * **35mm Anamorphic** :
    * **X** : 21.946
    * **Y** : 18.593
  * **65mm ALEXA** :
    * **X** : 54.12
    * **Y** : 25.59
  * **70mm** :
    * **X** : 52.476
    * **Y** : 23.012
  * **70mm IMAX** :
    * **X** : 70.41
    * **Y** : 52.63
  * **Custom** :
    * Set the **X** and **Y** values manually

  
If you change the **Sensor Size** values manually, Unity automatically sets this property to **Custom**.  
**Sensor Size** | Set the size, in millimeters, of the camera sensor.   
  
Unity sets the **X** and **Y** values automatically when you choose the **Sensor Type**.  
**X** | The horizontal size of the camera sensor.  
**Y** | The vertical size of the camera sensor.  
**ISO** | The light sensitivity of the camera sensor.  
**Shutter Speed** | The amount of time the camera sensor captures light.  
**Unit** | The unit of measurement for **Shutter Speed**.  
  
Available options:
  * **Second**
  * **1/Second**

  
**Gate Fit** | Options for changing the size of the **resolution gate** (size/aspect ratio of the game view) relative to the **film gate** (size/aspect ratio of the Physical Camera sensor).  
  
For more information about resolution gate and film gate, refer to the documentation on [Physical Cameras](https://docs.unity3d.com/Manual/PhysicalCameras.html).  
**Vertical** | Fits the resolution gate to the height of the film gate.  
  
If the sensor aspect ratio is larger than the game view aspect ratio, Unity crops the rendered image at the sides.  
  
If the sensor aspect ratio is smaller than the game view aspect ratio, Unity overscans the rendered image at the sides.  
  
When you choose this setting, any change to the sensor width (**Sensor Size** > **X**) has no effect on the rendered image.  
**Horizontal** | Fits the resolution gate to the width of the film gate.  
  
If the sensor aspect ratio is larger than the game view aspect ratio, Unity overscans the rendered image on the top and bottom.  
  
If the sensor aspect ratio is smaller than the game view aspect ratio, Unity crops the rendered image on the top and bottom.  
  
When you choose this setting, any change to the sensor height (**Sensor Size** > **Y**) has no effect on the rendered image.  
**Fill** | Fits the resolution gate to either the width or height of the film gate, whichever is smaller. This crops the rendered image.  
**Overscan** | Fits the resolution gate to either the width or height of the film gate, whichever is larger. This overscans the rendered image.  
**None** | Ignores the resolution gate and uses the film gate only. This stretches the rendered image to fit the game view **aspect ratio** The relationship of an image’s proportional dimensions, such as its width and height.  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#AspectRatio).  
## Lens
**Property** | **Description**  
---|---  
**Focal Length** | The distance, in millimeters, between the camera sensor and the camera lens.  
  
Lower values result in a wider **Field of View** , and vice versa.  
  
When you change this value, Unity automatically updates the **Field of View** property accordingly.  
**Shift** | Shifts the lens horizontally or vertically from center. Values are multiples of the sensor size; for example, a shift of 0.5 along the X axis offsets the sensor by half its horizontal size.  
  
You can use lens shifts to correct distortion that occurs when the camera is at an angle to the subject (for example, converging parallel lines).  
  
Shift the lens along either axis to make the camera frustum [oblique](https://docs.unity3d.com/Manual/ObliqueFrustum.html).  
**X** | The lens’s horizontal offset from the camera sensor.  
**Y** | The lens’s vertical offset from the camera sensor  
**Aperture** | The f-stop (f-number) of the lens. A lower value gives a wider lens aperture.  
**Focus Distance** | The distance from the camera where objects appear sharp when you enable Depth of Field.  
**Note** : When Physical Camera properties are in use at the same time as [Depth of Field](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/depth-of-field-urp.html)A post-processing effect that simulates the focus properties of a camera lens. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html)  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#DepthofField) **post-processing** A process that improves product visuals by applying filters and effects before the image appears on screen. You can use post-processing effects to simulate physical camera and film properties, for example Bloom and Depth of Field. [More info](https://docs.unity3d.com/6000.0/Documentation/Manual/PostProcessingOverview.html) post processing, postprocessing, postprocess  
See in [Glossary](https://docs.unity3d.com/6000.0/Documentation/Manual/Glossary.html#post-processing), the Lens properties directly affect the Depth of Field effect. This requires you to adjust both the Depth of Field properties and the Lens properties to create the effect you want.
## Aperture Shape
**Property** | **Description**  
---|---  
**Blade Count** | The number of blades in the lens aperture. A higher value gives a rounder aperture shape.  
**Curvature** | The curvature of the lens aperture blades.  
**Barrel Clipping** | The self-occlusion of the lens. A higher value creates a cat’s eye effect.  
**Anamorphism** | The amount of vertical stretch of the camera sensor to make the sensor taller or shorter. A higher value increases the stretch of the sensor to simulate an anamorphic look.  
* * *
[](https://docs.unity3d.com/6000.0/Documentation/Manual/urp/camera-component-reference.html)
Camera Inspector window reference for URP
[](https://docs.unity3d.com/6000.0/Documentation/Manual/cameras-birp.html)
Cameras in the Built-In Render Pipeline
