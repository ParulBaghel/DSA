class MyQueue {
    int f=0;
    int r=0;
    int[] q=new int [1000];
    public MyQueue() {
        
    }
    
    public void push(int x) {
        q[r]=x;
        r=r+1;

    }
    public int pop() {
        int x=q[f];
        f=f+1;
        return x;
    }
    
    public int peek() {
        return q[f];
    }
    
    public boolean empty() {
        if (f==r)
        {
            f=0;
            r=0;
            return true;
        }
        return false;
    }
}



/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */