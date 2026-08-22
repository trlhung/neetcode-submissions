using namespace std;
class MinStack {
private:
    stack<int> st;
    stack<int> minSt;
public:
    MinStack() {

    }
    
    void push(int val) {
        st.push(val);
        if (minSt.empty()) {
            minSt.push(val);
        }
        else {
            minSt.push(min(val, minSt.top()));
        }
    }
    
    void pop() {
        if (!st.empty()) {
            st.pop();
            minSt.pop();
        }
    }
    
    int top() {
        if (!st.empty()) {
            return st.top();
        }
    }
    
    int getMin() {
        if (!minSt.empty())
            {return minSt.top();}
    }
};
