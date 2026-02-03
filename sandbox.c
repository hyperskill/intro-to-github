#include "s21_decimal_struct.c"

unsigned divu10(unsigned n) {
  unsigned q, r;
  q = (n >> 1) + (n >> 2);
  q = q + (q >> 4);
  q = q + (q >> 8);
  q = q + (q >> 16);
  q = q >> 3;
  r = n - (((q << 2) + q) << 1);
  return q + (r > 9);
}

int main() {
  unsigned a = 1;
  unsigned b = 20;
  unsigned c = 100;

  // s21_decimal value_1 = {{a, 0, 0, (0 << 16) + (0 << 31)}};
  // s21_decimal value_2 = {{b, 0, 0, (0 << 16)}};
  // s21_decimal result = {{0, 0, 0, (0 << 16)}};

  // s21_div(value_1, value_2, &result);
  // printArrayBits_new(value_1.bits, 128);
  // printArrayBits_new(value_2.bits, 128);
  // printArrayBits_new(result.bits, 128);

  s21_BD bvalue_1 = {{0, 0, 0, a, 0, 0, 0, 0}};
  s21_BD bvalue_2 = {{b, 0, 0, 0, 0, 0, 0, 0}};
  s21_BD bresult = {0};
  s21_decimal test = {0};
  divide(bvalue_1, bvalue_2, &bresult);
  // BD_to_decimal(bresult,&test);

  // // printf("%u / %u = %f\n", a, b, (a * 1.0) / (b * 1.0));
  // printf("%u\n", bresult.bits[0]);
  
  printArrayBits_new(bvalue_1.bits, 224);
  // printArrayBits_new(bvalue_2.bits, 128);
  printf("OUT\n");
  printArrayBits_new(bresult.bits, 128);
  // printArrayBits_new(test.bits, 128);

  // test div_by_10

  // s21_BD value_div10 = {{0, 1, 0, 0, 0, 0, 0, 0}};
  // s21_BD res_div10 = {{0, 0, 0, 0, 0, 0, 0, 0}};
  // s21_BD ten = {{1000, 0, 0, 0, 0, 0, 0, 0}};

  // printArrayBits_new(value_div10.bits, 224);
  // printArrayBits_new(ten.bits, 224);
  // // printf("%u\n", value_div10.bits[0]);

  // divide(value_div10,ten,&res_div10);
  // // div_by_10(&value_div10);

  // printArrayBits_new(res_div10.bits, 256);
  // // printf("%u\n", res_div10.bits[0]);

  return 0;
}