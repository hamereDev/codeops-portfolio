
# Exercise 1: SRP (Single Responsibility Principle)


class ReportBuilder:
    def build(self):
        return 'Sales report data'


class ReportSaver:
    def save(self, report):
        print(f'Saving report: {report}')


class ReportEmailer:
    def email(self, report):
        print(f'Emailing report: {report}')


print('Exercise 1: SRP ')
builder = ReportBuilder()
report = builder.build()

saver = ReportSaver()
emailer = ReportEmailer()

saver.save(report)
emailer.email(report)



# Exercise 2: OCP (Open/Closed Principle)


class Shape:
    def area(self):
        return 0


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height


print('\nExercise 2: OCP ')
shapes = [
    Circle(3),
    Square(4),
    Triangle(6, 5)
]

for shape in shapes:
    print(f'{shape.__class__.__name__} area = {shape.area()}')



# Exercise 3: Singleton


class AppSettings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.currency = 'ETB'
        return cls._instance


print('\n  Exercise 3: Singleton ')
settings1 = AppSettings()
settings2 = AppSettings()

print('Currency:', settings1.currency)
print('Same object?', settings1 is settings2)



# Exercise 4: Factory


class ShapeFactory:
    @staticmethod
    def create(kind):
        if kind == 'circle':
            return Circle(2)
        elif kind == 'square':
            return Square(3)
        elif kind == 'triangle':
            return Triangle(4, 5)
        else:
            raise ValueError('Unknown shape type')


print('\n Exercise 4: Factory ')
shape1 = ShapeFactory.create('circle')
shape2 = ShapeFactory.create('square')
shape3 = ShapeFactory.create('triangle')

print('Circle area =', shape1.area())
print('Square area =', shape2.area())
print('Triangle area =', shape3.area())



# Exercise 5: Observer Pattern


class NewsAgency:
    def __init__(self):
        self.subscribers = []

    def subscribe(self, subscriber):
        self.subscribers.append(subscriber)

    def notify(self, news):
        for subscriber in self.subscribers:
            subscriber.update(news)


class EmailSubscriber:
    def update(self, news):
        print(f'[Email] Breaking news: {news}')


class MobileSubscriber:
    def update(self, news):
        print(f'[Mobile] Breaking news: {news}')


print('\n Exercise 5: Observer ')
agency = NewsAgency()

agency.subscribe(EmailSubscriber())
agency.subscribe(MobileSubscriber())

agency.notify('Fuel price updated in Addis Ababa')