function reverseWords(s: string): string {

    if (s.length < 1 || s.length > 1000) return "";
    const words = s.trim().split(" ").map(word => word.trim()).reverse().join(" ");
    return words.replace(/\s+/g, " ")
    
};