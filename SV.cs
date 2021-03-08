using System;
namespace DHP
{    class SV
    {
        // private int _MSSV;
        // private string _NameSV;
        // private double _DTB;
        // //Get
        // public int GetMSSV()
        // {
        //     return _MSSV;
        // }
        // //Set
        // public void SetMSSV(int mssv)
        // {
        //     _MSSV=mssv;
        // }
        // //Property
        // public string NameSV
        // {
        //     get
        //     {
        //         return _NameSV; 
        //     }
        //     set
        //     {
        //         _NameSV = value;
        //     }
        // }
        // public SV()
        // {
        //     _MSSV = 1;
        //     _NameSV="khong";
        //     _DTB=0.0;
        // }
        // public SV(int m, string n, double t)
        // {
        //     _MSSV = m;
        //     _NameSV=n;
        //     _DTB=t;
        // }
        // public SV(SV sv)
        // {
        //     _MSSV = sv._MSSV;
        //     _NameSV=sv._NameSV;
        //     _DTB=sv._DTB;
        // }
        // public int MSSV {get; set;}
        // public string NameSV {get; set;}
        // public double DTB {get; set;}
        // public void Show()
        // {
        //     Console.WriteLine("MSSV= {0}, Name= {1}, DTB= {2}", _MSSV, _NameSV, _DTB );
        // }
        // public SV(int m, string n, double t)
        // {
        //     MSSV = m;
        //     NameSV=n;
        //     DTB=t;
        //  }
        // public virtual void Show()
        // {
        //     Console.WriteLine("MSSV= {0}, Name= {1}, DTB= {2}", MSSV, NameSV, DTB );
        // }
        // public override string ToString()
        // {
        //     return "MSSV= " + MSSV + ", Name= " + NameSV + ", DTB= " + DTB;
        // }
        // public override bool Equals(object obj)
        // {
        //     return base.Equals(obj);
        // }
        // public void Thi()
        // {
        //     Console.WriteLine("Thi trac nghiem");
        // }

        public static bool CompareMSSV(object s1, object s2)
        {
            if(((SV)s1).MSSV>((SV)s1).MSSV)
            return true;
            else
            return false;
        }
        public static bool CompareNameSV(SV s1, SV s2)
        {
            if(String.Compare(((SV)s1).NameSV>((SV)s1).NameSV)>=0)
            return true;
            else
            return false;
        }
    }
}