/*

The goal for your program is to safely land the "Mars Lander" shuttle, the landing ship 
which contains the Opportunity rover. Mars Lander is guided by a program, and right now the failure 
rate for landing on the NASA simulator is unacceptable.

This puzzle is the second level of the "Mars Lander" trilogy. The controls are the same as 
the previous level but you must now control the angle in order to succeed.

	Rules

Built as a game, the simulator puts Mars Lander on a limited zone of Mars sky.
	The zone is 7000m wide and 3000m high.

There is a unique area of flat ground on the surface of Mars, which is at least 1000 meters wide.
Every second, depending on the current flight parameters (location, speed, fuel ...), 
the program must provide the new desired tilt angle and thrust power of Mars Lander:
	Angle goes from -90° to 90° . Thrust power goes from 0 to 4 .
  The game simulates a free fall without atmosphere. Gravity on Mars is 3.711 m/s² . 
  For a thrust power of X, a push force equivalent to X m/s² is generated and X liters of fuel are consumed. 
  As such, a thrust power of 4 in an almost vertical position is needed to compensate for the gravity on Mars.

For a landing to be successful, the ship must:
land on flat ground
land in a vertical position (tilt angle = 0°)
vertical speed must be limited ( ≤ 40m/s in absolute value)
horizontal speed must be limited ( ≤ 20m/s in absolute value)
 	Note

Tests and validators are only slightly different. A program that passes a given test will pass 
the corresponding validator without any problem.
*/

int main(){

  return 0;
}
