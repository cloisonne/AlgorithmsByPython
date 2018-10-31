#include <iostream>
using namespace std;

class Animal
{
    protected:
        char name[4] = "0";
        int age = 0;
        int height = 0;
        double weight = 0;

    public:
        Animal(){}
        ~Animal(){}
        virtual void Walk() = 0;
        virtual void Eat() = 0;
        virtual void Sleep() = 0;
};

class Dog: public Animal
{
    public:
        virtual void Walk(){};
        virtual void Eat(){};
        virtual void Sleep(){};
};

class Cat: public Animal
{
    public:
        virtual void Walk(){}
        virtual void Eat(){}
        virtual void Sleep(){}
};

int main()
{
    Animal *animal;
    Dog dog;
    animal = &dog;
    animal->Walk();
	return 0;
}