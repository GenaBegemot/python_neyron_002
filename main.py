# КАК ПОЛЬЗОВАТЬСЯ: сначала нужно обучить нейросеть на входных (input_data) и выходных данных (exp_result)
# например, перевод километров в мили:  в 1 км (input_data) 6,21 миля (exp_result)
# прогон по циклу while в конце
# после обучения полученные веса перенести в self.weight, закомментировать цикл обучения и выходные данные (exp_result)


class Neuron():
    def __init__(self):
        self.weight = 1.1
        self.last_error = 1.1
        self.smoothing = 0.000001

    def get_weight(self):
        return self.weight
    def get_last_error(self):
        return self.last_error
    def get_smoothing(self):
        return self.smoothing

    def process_input_data(self, input_data):
        return input_data * self.weight

    def train(self, input, exp_result):
        now_result = input * self.weight
        self.last_error = exp_result - now_result
        correction = self.last_error / now_result
        correction = correction * self.smoothing
        self.weight += correction

    def check_training(self):
        if(self.last_error > self.smoothing or self.last_error < -self.smoothing): return True
        else: return False


neuron = Neuron()
print("Перевод Километров в Мили с помощью обученной нейросети")
input_data = int(input("Введите данные (км): "))         # входное значение (километры)
# exp_result = int(input("Введите данные (мили): "))       # ожидаемый результат (мили) -> закомментировать после завершения обучения
print(f"Результат перевода Километров в Мили:  {neuron.process_input_data(input_data)}")


# процесс обучений нейросети
# iteration = 1
# while (neuron.check_training()):
#     neuron.train(input_data, exp_result)
#     iteration += 1
# print(f"Обучение завершено за {iteration} циклов")
# print(f"Вес: {neuron.get_weight()}")
# print(f"Результат: {neuron.process_input_data(input_data)}")