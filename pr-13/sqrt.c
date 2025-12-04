float Q_rsqrt( float number )
{
	long i;
	float x2, y;
	const float threehalfs = 1.5F;

	x2 = number * 0.5F;
	y  = number;
	i  = * ( long * ) &y;                       // страшное дробное хакерство на битовом уровне
	i  = 0x5f3759df - ( i >> 1 );               // что за чёрт?
	y  = * ( float * ) &i;
	y  = y * ( threehalfs - ( x2 * y * y ) );   // 1-я итерация
//	y  = y * ( threehalfs - ( x2 * y * y ) );   // 2-я итерация, можно убрать

	return y;
}