## Controllability Matrix \( \mathcal{C} \):

$$
\mathcal{C} = \begin{bmatrix}
0 & 0 & 0 & -\frac{k}{J_l J_m} & \frac{B_l k}{J_l^2 J_m} + \frac{B_m k}{J_l J_m^2} + \frac{k k_t}{J_l J_m L_a} \\
0 & 0 & -\frac{k}{J_l J_m} & \frac{B_l k}{J_l^2 J_m} + \frac{B_m k}{J_l J_m^2} + \frac{k k_t}{J_l J_m L_a} & \frac{k^2}{J_l^2 J_m} + \frac{B_l k^2}{J_l^3 J_m} + \frac{B_m k^2}{J_l^2 J_m^2} + \frac{k^2 k_t}{J_l^2 J_m L_a} \\
0 & -\frac{1}{J_m} & \frac{B_m}{J_m^2} + \frac{k_t}{J_m L_a} & \frac{k}{J_m^2} - \frac{B_m^2}{J_m^3} - \frac{B_m k_t}{J_m^2 L_a} - \frac{k_t R_a}{J_m L_a^2} & -\frac{k^2}{J_l J_m^2} - \frac{B_m k^2}{J_l J_m^3} - \frac{k^2 k_t}{J_l J_m^2 L_a} - \frac{k_t R_a k}{J_l J_m L_a^2} \\
-\frac{1}{J_m} & \frac{B_m}{J_m^2} + \frac{k_t}{J_m L_a} & \frac{k}{J_m^2} - \frac{B_m^2}{J_m^3} - \frac{B_m k_t}{J_m^2 L_a} - \frac{k_t R_a}{J_m L_a^2} & -\frac{B_m k}{J_m^3} - \frac{k k_t}{J_m^2 L_a} + \frac{B_m^3}{J_m^4} + \frac{B_m^2 k_t}{J_m^3 L_a} + \frac{B_m k_t R_a}{J_m^2 L_a^2} + \frac{k_t^2}{J_m^2 L_a} + \frac{k_t R_a^2}{J_m L_a^3} & -\frac{B_m k^2}{J_l J_m^3} - \frac{k^2 k_t}{J_l J_m^2 L_a} + \frac{B_m^3 k}{J_l J_m^4} + \frac{B_m^2 k k_t}{J_l J_m^3 L_a} + \frac{B_m k k_t R_a}{J_l J_m^2 L_a^2} + \frac{k_t^2 k}{J_l J_m^2 L_a} + \frac{k_t R_a^2 k}{J_l J_m L_a^3} \\
\frac{1}{L_a} & -\frac{R_a}{L_a^2} & \frac{k_t}{J_m L_a} + \frac{R_a^2}{L_a^3} & -\frac{B_m k_t}{J_m^2 L_a} - \frac{k_t^2}{J_m L_a^2} - \frac{R_a k_t}{J_m L_a^2} - \frac{R_a^3}{L_a^4} & -\frac{k_t k^2}{J_l J_m^2 L_a} - \frac{k_t^2 k}{J_l J_m L_a^2} - \frac{R_a k_t k}{J_l J_m L_a^2} - \frac{R_a^3 k}{J_l L_a^4}
\end{bmatrix}
$$

## Determinant of Controllability Matrix:

$$
\text{det}(\mathcal{C}) = \frac{k^2 \left( B_l L_a^3 k_t^2 + J_l L_a^2 k_t^3 + J_l J_m R_a^4 + J_l J_m k_t^4 + L_a^4 k k_t + B_l J_m L_a k_t^3 + B_m J_l L_a k_t^3 - B_l L_a^3 R_a k - B_m L_a^3 R_a k - B_l L_a^3 R_a k_t - 4 J_l J_m R_a k_t^3 - 4 J_l J_m R_a^3 k_t + B_l L_a^3 k k_t + B_m L_a^3 k k_t + B_l B_m L_a^2 R_a^2 + B_l B_m L_a^2 k_t^2 + 6 J_l J_m R_a^2 k_t^2 + J_l L_a^2 R_a^2 k + J_m L_a^2 R_a^2 k - 2 J_l L_a^2 R_a k_t^2 + J_l L_a^2 R_a^2 k_t + J_l L_a^2 k k_t^2 + J_m L_a^2 k k_t^2 - B_l J_m L_a R_a^3 - B_m J_l L_a R_a^3 - 2 B_l B_m L_a^2 R_a k_t - 3 B_l J_m L_a R_a k_t^2 + 3 B_l J_m L_a R_a^2 k_t - 3 B_m J_l L_a R_a k_t^2 + 3 B_m J_l L_a R_a^2 k_t - 2 J_l L_a^2 R_a k k_t - 2 J_m L_a^2 R_a k k_t \right)}{J_l^3 J_m^5 L_a^5}
$$

## Observability Matrix \( \mathcal{O} \):

$$
\mathcal{O} = \begin{bmatrix}
1 & 0 & 0 & 0 & 0 \\
0 & 1 & 0 & 0 & 0 \\
-\frac{k}{J_l} & -\frac{B_l}{J_l} & \frac{k}{J_l} & 0 & 0 \\
\frac{B_l k}{J_l^2} & \frac{B_l^2}{J_l^2} - \frac{k}{J_l} & -\frac{B_l k}{J_l^2} & \frac{k}{J_l} & 0 \\
\frac{k^2}{J_l^2} - \frac{B_l^2 k}{J_l^3} + \frac{k^2}{J_l J_m} & \frac{B_l k}{J_l^2} + \frac{B_l \left( \frac{k}{J_l} - \frac{B_l^2}{J_l^2} \right)}{J_l} & \frac{B_l^2 k}{J_l^3} - \frac{k^2}{J_l^2} - \frac{k^2}{J_l J_m} & -\frac{B_l k}{J_l^2} - \frac{B_m k}{J_l J_m} & \frac{k k_t}{J_l J_m}
\end{bmatrix}
$$

## Determinant of Observability Matrix:

$$
\text{det}(\mathcal{O}) = \frac{k^3 k_t}{J_l^3 J_m}
$$
