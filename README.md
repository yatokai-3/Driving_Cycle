## Development of driving cycle and estimation of associated emmissions

The main focus of this project is to generate emission data using the real-world
driving cycle. Driving Cycle uses the vehicular data moving from one location to another from different routes every time to experience different driving
patterns and gather data as random as possible.

#### What is Driving Cycle.
A driving cycle is a predefined speed-time profile that represents typical driving patterns of a vehicle. It provides a standardized way to evaluate and compare vehicles' fuel efficiency and other performance characteristics under similar conditions.

#### Steps done to perform the projects-
- Calculated the parameters of the original driving cycle. Parameters include average speed, Kinetic energy, average acceleration, average deceleration, root mean square acceleration, etc 
- Generation of Micro Trips Development of a drive cycle is based on micro-trips. Micro-trip is an excursion between two successive time points at which the vehicle is stopped. And threshold speed considered here is 0.7m/s, i.e., the range of speed between the (0-0.7m/s) believe to be 0m/s.
- Data Analysis portion where driving cycle generated by smooth connection between micro trips for that particular condition applied. The difference between the Tail and the Head value of two consecutive micro trips should be less than 0.4m/s and developed a potential driving cycle for varanasi city. 
- Computated parameters of potential driving cycle and compare it with the parameter of original driving cycle. 8 Potential Driving Cycle were formed during my run of code. If value differs too much generate another list of potential driving cycle. 

#### Results
<table>
  <tr>
    <td align="center">
      <img src="https://github.com/yatokai-3/yatokai-3/assets/111629438/c22aa1e6-0c4d-46d3-884f-62232a596a56" alt="CAD" width="500">
      <p>Fig. 1 Developed Driving Cycle of Varanasi</p>
    </td>
    <td align="center">
      <img src="https://github.com/yatokai-3/yatokai-3/assets/111629438/5e67638d-a769-40ee-9040-41ff5658e4e5" alt="Mesh" width="500">
      <p>Fig. 2 European Driving Cycle(EUDC)</p>
    </td>
  </tr>


  <tr>
    <td align="center">
     <img src="https://github.com/yatokai-3/yatokai-3/assets/111629438/5b54a614-3077-4090-b3a3-f1830486dce1" alt="Image 4" width="500">
      <p>Fig. 3 Comparison between the vehicular parameters of varanasi and standard driving cycle (IDC and EUDC).</p>
    </td>
    <td align="center">
      <img src="https://github.com/yatokai-3/yatokai-3/assets/111629438/6df29df6-10ef-4142-96e5-c9a2a667bb5a" alt="Image 4" width="500">
      <p>Fig. 4 Comparison between the emission parameters of varanasi and standard driving cycle.</p>
    </td>
  </tr>
  <tr>
    <td align="center">
     <img src="https://github.com/yatokai-3/Driving_Cycle/assets/111629438/1e3668e0-1b5b-4430-a075-68ac687d3141" alt="Image" width="500">
      <p>Fig. 5 Comparison between parameter of original Driving cycle and Driving Cycle created .</p>
    </td>
    <td align="center">
      <img src="https://github.com/yatokai-3/Driving_Cycle/assets/111629438/a16fa820-af8f-4f9a-a2d4-a1205ab826be" alt="Imagex" width="500">
      <p>Fig. 6 All parameters of all the 8 potential driving cycle.</p>
    </td>
  </tr>
</table>
