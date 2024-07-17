DESCRIPTION
	The Pyro Head-Gear is a technology that provides assistance to the fire fighters by providing necessary information during the rescue or firefighting mission to plan their strategies for their situation.

Pyro Head-gear aims at providing assistance to the modern age fire-fighters by augmented reality technology. The Augmented reality allows the software to interact with the visual perspective of the fire-fighter and providing him updates of his environment. GPS allows him to keep track of his team-mates and vice-versa. 
The Pyro Head-gear consists of 3 modules. A three Dimensional AR-map which allows the user to track his team, an embedded system which gets the sensor input and transfer it to the main processor, the HUD which integrates the data from the other two modules and renders an AR display.
AUGMENTED REALITY MODULE
The 3-Dimentional map is created and uses GPS co-ordinates for its orientation. To send and receive the co-ordinates between the team, an android APK is utilized. The APK is designed on android platform. The GPS data is collected from the android device and uploaded to a data base. The collected data is then downloaded in the main processor. A custom algorithm is then used to map the co-coordinates. The 3D map’s abstract elements are designed in 3DS max. The Radar planes along with field marker models are developed and they are exported into the Unity software. 
IMAGE RENDERING
The data from image processing acts as a reference for the software to interact with the real world and this way, the orientation and model developed or downloaded is rendered with reference to the glyph. The reference includes the size and the angle of the render.
 The movements of the Team mates are recognized with the GPS positioning and they are used to orient with respective to the First-person. 
Thus by co-ordination both the android applications, cross platform data transfer is possible. Cloud servers instead of SQL servers can further increase the performance.
EMBEDDED SYSTEM MODULE
 The Embedded network uses a Linux based RTOS patch for real time data reception and an ADB protocol for data transfer. The Raspberry Pi provides hardware support. It receives the data from MQ7 and DB18S20 sensors. The MQ7 is uses to know the percentage of CO2 in the surroundings and DB18S20 is a temperature sensor. The feed from these sensors are received from the digital input pins of the raspberry. The Raspbian Kernel is re-programmed by a Xenomai patch to work as a Real-time OS providing fast updates on the transmission and reception data. The Linux uses shell programming coded in Python and the sensor data is saved in a XML file. This XML file is transferred to the main Memory by the ADB and then utilized by Unity.
FILE TRANSFER
	The file transfer is done by using Extensible markup language(XML) and Android Debug Bridge(ADB).
EXTENSIBLE MARKUP LANGUAGE
The usage of XML is very advantages since it had a good support with Unity game engine and also it uses standard web protocols and this allows the developers to include larger data during transfer with less update rates. XML also has the advantage of all the web support features and hence standard TCP can be replaced by advanced database file transfer techniques such as cloud. Cloud servers could be used for both file transfer and also maintaining a report log for every fire safety incident.
ANDROID DEBUG BRIDGE
File transfers are made in the most universal protocols. They are implemented in such a way that they are not platform specific. Although the Android Debugging Bridge plug-in are added to the Linux Kernel, it uses standard TCP for file transfer and any devices other than Android doesn't require any other plug-in to be interfaced with it. This is a major advantage in developing cross platform modules.
DISPLAY MODULE
 Finally the HUD is designed in Unity game engine which uses C# programming language and this is projected in a display which acts as a see through for the fire fighters. Stereoscopic render is possible via Unity Engine.

 Screenshots:
https://github.com/KoviElango/PyroHeadGear/blob/main/glyphmap.png
